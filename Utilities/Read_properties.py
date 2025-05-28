import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class Read_config:
    @staticmethod
    def get_snapdeal_url():
        url=config.get('snapdeal info','snap_deal_page')
        return url

    @staticmethod
    def get_shoe_name():
        mens_shoe=config.get('snapdeal info','product_name')
        return mens_shoe