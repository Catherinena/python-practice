from .sql import Sql
from dingdian.items import DingdianItem


class DingdianPipeline(object):

    def process_item(self, item, spider):

        if isinstance(item, DingdianItem):
            name_id = item['nameId']
            ret = Sql.select_name(name_id)
            if ret[0] == 1:
                print('已经存在')
                pass
            else:
                xs_name = item['name']
                xs_author = item['author']
                xs_url = item['novelUrl']
                xs_status = item['serialStatus']
                xs_number = item['serialNumber']
                xs_name_id = item['nameId']
                Sql.insert_dingdian_item(xs_name, xs_author, xs_url, xs_status, xs_number, xs_name_id)
                print("开始存储...")
