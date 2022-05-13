import yaml
import dash_html_components as html
from dash_component import RCTree as dash_tree
from objects_handle import LocalObjectsHandle

class TreeView:

    _tree_views = {}

    def __init__(self, app, user_id, session_id, SessionsManager):
        unique_id = f"tree-{user_id}-{session_id}"
        tree_state = TreeView._tree_views.get(unique_id)
        if not tree_state:
            TreeView._tree_views[unique_id] = self.__dict__
            self._SessionsManager = SessionsManager
            self._user_id = user_id
            self._unique_id = unique_id
            self._session_id = session_id
            self._app = app
        else:
            self.__dict__ = tree_state

    def populate_tree(self, data):
        children = []
        keys = []
        for item_name, item_data in data.items():
            tree_data = {}
            tree_data["title"] = item_name
            icon = item_data.get("icon")
            remote = item_data.get("remote")
            local = item_data.get("local")
            index = item_data.get("index", "")

            key = item_name
            if local:
                key = f"local:{local}:{index}"
            elif remote:
                key = f"remote:{remote}:{index}"

            tree_data["key"] = key
            keys.append(key)
            tree_data["icon"] = icon

            if item_data.get("children"):
                tree_data["children"], child_keys = self.populate_tree(
                    item_data["children"]
                )
                keys = keys + child_keys
            elif local:
                handle = LocalObjectsHandle(self._SessionsManager)
                indices = handle.get_child_indices(
                    self._user_id,
                    self._session_id,
                    f"{local}-{index}" if index else local,
                )
                if indices:
                    children_data = {
                        f"{local}-{index}": {
                            "local": f"{local}",
                            "index": f"{index}",
                            "icon": icon,
                        }
                        for index in indices
                        if index
                    }
                    tree_data["children"], child_keys = self.populate_tree(
                        children_data
                    )
                    keys = keys + child_keys
            elif remote:
                static_info = self._SessionsManager(
                    self._app, self._user_id, self._session_id
                ).static_info
                obj = self._SessionsManager(
                    self._app, self._user_id, self._session_id
                ).settings_root
                path_list = remote.split("/")

                for path in path_list:
                    try:
                        obj = getattr(obj, path)
                        static_info = static_info["children"][obj.obj_name]
                    except AttributeError:
                        obj = obj[path]
                        static_info = static_info["object-type"]
                if static_info["type"] == "named-object":
                    if not obj.is_active():
                        continue
                    children_name = list(obj.get_state().keys())
                    if children_name:
                        tree_data["key"] = item_name
                        children_data = {
                            child: {"remote": f"{remote}/{child}", "icon": icon}
                            for child in children_name
                        }
                        tree_data["children"], child_keys = self.populate_tree(
                            children_data
                        )
                        keys = keys + child_keys
            children.append(tree_data)

        return children, keys

    def get_tree_nodes(
        self,
        yaml_file="E:\\ajain\\ANSYSDev\\vNNN\\pyfluent\\src\\ansys\\fluent\\core\\utils\\dash\\outline.yaml",
    ):

        with open(yaml_file) as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
            tree_nodes, keys = self.populate_tree(data)
        return tree_nodes[0], keys
