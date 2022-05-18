from typing import List

from compose_viz.extends import Extends


class Service:
    def __init__(self, name: str, image: str = None, ports: List[str] = [], networks: List[str] = [], volumes: List[str] = [], depends_on: List[str] = [], links: List[str] = [], extends: Extends = None) -> None:
        self._name = name
        self._image = image
        self._ports = ports
        self._networks = networks
        self._volumes = volumes
        self._depends_on = depends_on
        self._links = links
        self._extends = extends

    @property
    def name(self):
        return self._name

    @property
    def image(self):
        return self._image

    @property
    def ports(self):
        return self._ports

    @property
    def networks(self):
        return self._networks

    @property
    def volumes(self):
        return self._volumes

    @property
    def depends_on(self):
        return self._depends_on

    @property
    def links(self):
        return self._links

    @property
    def extends(self):
        return self._extends
