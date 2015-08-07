import logging
import sys
import time
import os

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from geobricks_common.core.filesystem import get_filename, get_file_extension

from geobricks_geoserver_manager.config.config import config
from geobricks_geoserver_manager.core.geoserver_manager_core import GeoserverManager


logging.basicConfig(level=logging.ERROR)


class MyEventHandler(FileSystemEventHandler):
    def __init__(self, observer):
        self.observer = observer

    def on_created(self, event):
        print "e=", event
        print event.src_path
        # ['src_path']
        path = event.src_path
        folder, filename, name = get_filename(path, True)
        ext = get_file_extension(path)
        print path
        print filename
        print name
        print ext
        if ext == 'shp':
            base_path = os.path.abspath(os.path.join(folder, name))
            p = {
                'shp': base_path + '.shp',
                'shx': base_path + '.shx',
                'dbf': base_path + '.dbf',
                'prj': base_path + '.prj'
            }
            data = {
                "layerName": name,
                "workspace": "workspace_test",
            }
            print 'publish shapefile'
            print p, data
            geoserver_manager = GeoserverManager(config)
            print len(geoserver_manager.gs_slaves)
            result = geoserver_manager.publish_shapefile(p, data, True)
            print result

        if ext == 'sld':
            geoserver_manager = GeoserverManager(config)
            result = geoserver_manager.publish_style(path)



    def on_deleted(self, event):
        print "e=", event
        print event.src_path
        path = event.src_path
        folder, filename, name = get_filename(path, True)
        ext = get_file_extension(path)
        if ext == 'shp':
            geoserver_manager = GeoserverManager(config)
            print len(geoserver_manager.gs_slaves)
            result = geoserver_manager.delete_store(name, "workspace_test")
            print result


if __name__ == "__main__":
    path = "data/"

    observer = Observer()
    event_handler = MyEventHandler(observer)

    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    observer.join()