class PlazaPipeline:
    def process_item(self, item, spider):
        '''
        define 3 mood for register in phone
        :param item:
        :return: item
        '''

        if 'گوشی' in item['title']:

            if 'رجیستری' in item['register']:
                item['register'] = 'رجیستر شده'

            elif item['register'] is None:
                item['register'] = 'نامشخص '

            else:
                item['register'] = 'رجیستر نشده'
        else:
            item['register'] = []

        return item
