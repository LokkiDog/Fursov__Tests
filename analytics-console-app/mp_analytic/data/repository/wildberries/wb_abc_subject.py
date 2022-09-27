from data.utils.functions import get_profit, get_turnover, get_abc


class ABCSubjectReport:
    def __init__(self):
        self.response = {}

    def execute(self, profitability, dynamic, stocks):
        self.__get_profitability(profitability)
        self.__get_turnover(dynamic, stocks)
        self.__subject_group()
        return self.__get_table()

    def __get_profitability(self, profitability):
        for row in profitability:
            op = row[10]
            rub = row[6]

            article = row[4].split('/')[0]
            if self.response.get(article):
                if type(op) != str and type(self.response[article]['op']) != str:
                    self.response[article]['op'] += op
                elif type(self.response[article]['op']) == str and type(op) != str:
                    self.response[article]['op'] = op
                self.response[article]['rub'] += rub
            else:
                self.response[article] = {'subject': row[2], 'article': article, 'op': op, 'rub': rub, 'dynamic': '-',
                                          'stocks': '-'}

    def __get_turnover(self, dynamic, stocks):
        for row in dynamic:
            article = row[4].split('/')[0]
            if self.response.get(article):
                if type(self.response[article]['dynamic']) != str:
                    self.response[article]['dynamic'] += row[-1]
                else:
                    self.response[article]['dynamic'] = row[-1]
            else:
                self.response[article] = {'subject': row[2], 'article': article, 'op': '-', 'rub': '-',
                                          'dynamic': row[-1], 'stocks': '-'}

        for row in stocks:
            article = row[3].split('/')[0]
            if self.response.get(article):
                if type(self.response[article]['stocks']) != str:
                    self.response[article]['stocks'] += row[-1]
                else:
                    self.response[article]['stocks'] = row[-1]
            else:
                self.response[article] = {'subject': '-', 'article': article, 'op': '-', 'rub': '-',
                                          'dynamic': '-', 'stocks': row[-1]}

    def __subject_group(self):
        sub_dict = {}
        for article in self.response.values():
            if sub_dict.get(article['subject']):
                op = article['op']
                rub = article['rub']
                if type(op) != str and type(sub_dict[article['subject']]['op']) != str:
                    sub_dict[article['subject']]['op'] += op
                elif type(sub_dict[article['subject']]['op']) == str and type(op) != str:
                    sub_dict[article['subject']]['op'] = op

                if type(rub) != str and type(sub_dict[article['subject']]['rub']) != str:
                    sub_dict[article['subject']]['rub'] += rub
                elif type(sub_dict[article['subject']]['rub']) == str and type(rub) != str:
                    sub_dict[article['subject']]['op'] = rub

                if type(sub_dict[article['subject']]['dynamic']) != str:
                    sub_dict[article['subject']]['dynamic'] += article['dynamic']
                elif type(sub_dict[article['subject']]['dynamic']) == str:
                    sub_dict[article['subject']]['dynamic'] = article['dynamic']

                if type(sub_dict[article['subject']]['stocks']) != str and type(article['stocks']) != str:
                    sub_dict[article['subject']]['stocks'] += article['stocks']
                elif type(article['stocks']) != str:
                    sub_dict[article['subject']]['stocks'] = article['stocks']
            else:
                sub_dict[article['subject']] = {'subject': article['subject'], 'op': article['op'],
                                                'rub': article['rub'], 'dynamic': article['dynamic'],
                                                'stocks': article['stocks']}
        self.response = sub_dict

    def __get_table(self):
        table = [["Предмет", "Рентабельность", "Оборачиваемость", "Итог"]]

        for article in self.response.values():
            if article['op'] != '-' and article['rub'] != '-':
                if article['rub'] != 0:
                    profit = round(article['op'] / article['rub'] * 100)
                    if article['op'] < 0 and article['rub'] < 0:
                        profit *= -1
                else:
                    profit = '-'
            else:
                profit = '-'
            profit_letter = get_profit(profit) if profit != '-' else '-'

            if article['dynamic'] != '-' and article['stocks'] != '-':
                if article['dynamic'] != 0:
                    turnover = round(article['stocks'] / (article['dynamic'] / 7) * 100)
                else:
                    turnover = '-'
            else:
                turnover = '-'
            turnover_letter = get_turnover(turnover) if turnover != '-' else '-'

            if profit_letter != '-' and turnover_letter != '-':
                abc = get_abc(profit_letter, turnover_letter)
            else:
                abc = '-'
            row = [article['subject'], profit_letter, turnover_letter, abc]
            table.append(row)
        return table
