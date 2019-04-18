#coding:utf-8

from urllib import request, parse
from bs4 import BeautifulSoup
import time
import re
import time
import copy
import random

def find_a_year(url,
                referer,
                date_begin,
                date_end,
                pageNum,
                keyWord):

    # 查询和检索文章的地址不一样
    url = url

    # 文件头包含浏览器属性和REFERER属性
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
        'Referer': referer,
        # 'Cookie':'JSESSIONID=7062C0FCA3762756C7A7E01EAD10B932; targetEncodinghttp://127001=2'
        'Cookie':'_pk_id.2.6daf=9b1a63177d9c7635.1554870540.2.1554901008.1554901008.; JSESSIONID=CDFFA36036E624378EFC02CC6E53C66B; targetEncodinghttp://127001=2; _pk_ses.2.6daf=*'
    }

    # 数据包含明文与非明文
    # data = {
    #     "日期".encode('gbk'):"",
    #     "标题".encode('gbk'):"",
    #     "版次".encode('gbk'):1,
    #     "版名".encode('gbk'):"",
    #     "作者".encode('gbk'): "",
    #     "专栏".encode('gbk'): "",
    #     "正文".encode('gbk'): "三农".encode('gbk'),
    #     "Relation": "AND",
    #     "sortfield": "RELEVANCE",
    #     "searchword": "版次=(1) AND 正文=(三农)".encode('gbk'),
    #     "presearchword": "版次=(1) AND 正文=(三农)".encode('gbk'),
    #     "channelid":16380,
    #     "image1.x":0,
    #     "image1.y":0,
    # }
    data = {
        "qs":""
    }

    # 这个函数生成data
    # def data_gen():


    # 这个函数生成询问字串
    def searchkey(data, date_begin, date_end, word):

        qs = '{"cIds":"","cds":[{"fld":"dataTime.start","cdr":"AND","hlt":"false","vlr":"AND","qtp":"DEF","val":"'+date_begin+'"},{"fld":"dataTime.end","cdr":"AND","hlt":"false","vlr":"AND","qtp":"DEF","val":"'+date_end+'"},{"cdr":"AND","cds":[{"fld":"contentText","cdr":"AND","hlt":"true","vlr":"AND","qtp":"DEF","val":"'+word+'"}]}],"obs":[{"fld":"dataTime","drt":"DESC"}]}'
        data['qs'] = qs

        return data

    def searchnum(data, articleuum):

        data['pageSize'] = articleuum

        return data

    # 这个函数返回搜索的页面
    def searchpage(url, headers, data):

        req = request.Request(url=url, headers=headers, data=data)
        response = request.urlopen(req)
        page = response.read()
        # page = response.read().decode('gbk')
        soup = BeautifulSoup(page, 'html.parser')

        return soup

    # 开始爬虫
    def finish(url, headers, data):
        print("begin with", time_seg)
        # 页码数
        data_tmp = parse.urlencode(data).encode('utf-8')
        time.sleep(time_seg * random.random())
        soup = searchpage(url, headers, data_tmp)
        numstr = soup.find('li', {'class':'disabled controls'}).get_text()
        num = int(re.search('\d+',numstr).group())

        for i in range(pageNum, num):
            # 提取第i页
            global pageError
            pageError = i

            articles = []
            data['pageNo'] = i+1
            data_tmp = parse.urlencode(data).encode('utf-8')
            time.sleep(time_seg * random.random())
            soup = searchpage(url, headers, data_tmp)


            for j in range(len(soup.select('.articleSum_li'))):
                print(i+1, j+1, date_begin, date_end)

                article = soup.select('.articleSum_li')[j]
                title = article.h2.a.get_text()

                date = soup.select('.news_sum_bottom')[j].select('span')[1].get_text()
                date = date.split()[-1]

                url_tmp = 'http://data.people.com.cn' + article.h2.a['href']
                print(url_tmp)

                # url_tmp = 'http://data.people.com.cn/sc/detail'
                r = re.search('\d+.*', article.h2.a['href'])
                data_tmp = {
                    'articleId':r.group()
                }
                data_tmp = parse.urlencode(data_tmp).encode('utf-8')

                time.sleep(time_seg * random.random())
                soup_2 = searchpage(url_tmp, headers, data_tmp)

                blackwords_list = soup_2.select('p')
                blackwords = [" ".join(b.get_text().split()) for b in blackwords_list]
                blackwords = " ".join(blackwords)
                articles.append(title + '\t' + date + '\t' + blackwords + '\n')

            with open('C:\\Users\\chenj\\Desktop\\renmin\\' + keyWord + '-' + date_begin + '-' + date_end + '.txt',
                      'a') as f:
                for a in articles:
                    f.write(a)
        global finish
        finish = 1
        return

    def finish_v2(url, headers, data):

        article_list = []
        soup = searchpage(url, headers, data=data)
        articles = soup.findAll(is_article_page)
        for article in articles:
            time.sleep(3)
            url = article.parent.parent['href']
            sp = searchpage(url, headers, data=None)
            text = sp.findAll(is_key_word)
            bt = text[0].get_text()
            zz = text[1].get_text()
            rq = text[2].get_text()
            bc = text[3].get_text()
            bm = text[4].get_text()
            para = sp.find(is_para).get_text()
            article_list.append(bt+'\t'+zz+'\t'+rq+'\t'+bc+'\t'+bm+'\t'+para)
            print(article_list)
        while soup.find(is_next_page) is not None:
            next_page = soup.find(is_next_page)
            url = next_page['href']
            soup = searchpage(url, headers, data=None)
            articles = soup.findAll(is_article_page)
            for article in articles:
                time.sleep(3)
                url = article.parent.parent['href']
                sp = searchpage(url, headers, data=None)
                text = sp.findAll(is_key_word)
                bt = text[0].get_text()
                zz = text[1].get_text()
                rq = text[2].get_text()
                bc = text[3].get_text()
                bm = text[4].get_text()
                para = sp.find(is_para).get_text()
                article_list.append(bt + '\t' + zz + '\t' + rq + '\t' + bc + '\t' + bm + '\t' + para)
                print(article_list)
        return article_list


    def is_next_page(tag):
        return tag.name=='a' and tag.img is not None and tag.img.has_attr('alt') and tag.img['alt']=="下一页"
    def is_article_page(tag):
        return tag.name=='span' and tag.has_attr('class') and tag.parent.name=='font'
    def is_key_word(tag):
        return tag.name=='td' and not tag.has_attr('height') and tag.a is None
    def is_para(tag):
        return tag.name=='div'

    data = searchkey(data, date_begin, date_end, keyWord)

    finish(url, headers, data=data)
    # url = 'http://data.people.com.cn/sc/detail?articleId=064503fca6f64ddc9f69127a3a4c88aa'
    # soup = searchpage(url, headers, None)
    # print(soup)


url = 'http://data.people.com.cn/sc/ss'
referer = 'http://data.people.com.cn/sc/'
keyWordlist = ['农民', '农业', '农村', '三农']
time_seg = 5
time_del = 2
count = -1
pageError = 0
finish = 0
date_begin = None
date_end = None

for keyWord in keyWordlist[:1]:
    # date_begin = '1946-05-15'
    # date_end = '1946-12-31'
    # pageNum = 0
    # while not finish:
    #     try:
    #         if count == -1:
    #             count += 1
    #             find_a_year(url, referer, date_begin, date_end, pageNum, keyWord)
    #         elif count >= 0:
    #             with open('C:\\Users\\chenj\\Desktop\\log.txt', 'r') as f:
    #                 log = f.readlines()[-1]
    #                 logstr = log.split()
    #                 date_begin = logstr[0]
    #                 date_end = logstr[1]
    #                 pageNum = int(logstr[2])
    #             find_a_year(url, referer, date_begin, date_end, pageNum, keyWord)
    #             if count > 0:
    #                 time_seg /= 2
    #             count = 0
    #     except:
    #         print("429 Error")
    #         count += 1
    #         time_seg += time_del
    #         with open('C:\\Users\\chenj\\Desktop\\log.txt', 'a') as f:
    #             f.write(date_begin + ' ' + date_end + ' ' + str(pageError) + '\n')


    date_begin = '1947-01-11'
    date_end = '1947-12-31'
    pageNum = 110
    while not finish:
        try:
            if count == -1:
                count += 1
                find_a_year(url, referer, date_begin, date_end, pageNum, keyWord)
            elif count >= 0:
                with open('C:\\Users\\chenj\\Desktop\\log.txt', 'r') as f:
                    log = f.readlines()[-1]
                    logstr = log.split()
                    date_begin = logstr[0]
                    date_end = logstr[1]
                    pageNum = int(logstr[2])
                find_a_year(url, referer, date_begin, date_end, pageNum, keyWord)
                if count > 0:
                    time_seg /= 2
                count = 0
        except Exception as err:
            print(err, time_seg)
            count += 1
            time_seg += time_del
            with open('C:\\Users\\chenj\\Desktop\\log.txt', 'a') as f:
                f.write(date_begin + ' ' + date_end + ' ' + str(pageError) + '\n')
    count = -1
    pageNum = 0
    pageError = 0

    finish = 0
    for i in range(1948, 2019):
        count = -1
        pageError = 0
        finish = 0
        date_begin = '%d-01-01' %i
        date_end = '%d-12-31' %i
        while not finish:
            try:
                if count == -1:
                    count += 1
                    find_a_year(url, referer, date_begin, date_end, 0, keyWord)
                elif count >= 0:
                    with open('C:\\Users\\chenj\\Desktop\\log.txt', 'r') as f:
                        log = f.readlines()[-1]
                        logstr = log.split()
                        date_begin = logstr[0]
                        date_end = logstr[1]
                        pageNum = int(logstr[2])
                    find_a_year(url, referer, date_begin, date_end, pageNum, keyWord)
                    if count > 0:
                        time_seg /= 2
                    count = 0
            except Exception as err:
                print(err, time_seg)
                count += 1
                time_seg += time_del
                with open('C:\\Users\\chenj\\Desktop\\log.txt', 'a') as f:
                    f.write(date_begin + ' ' + date_end + ' ' + str(pageError) + '\n')

    count = -1
    pageNum = 0
    pageError = 0

    finish = 0
    date_begin = '2019-01-01'
    date_end = '2019-04-09'
    while not finish:
        try:
            if count == -1:
                count += 1
                find_a_year(url, referer, date_begin, date_end, 0, keyWord)
            elif count >= 0:
                with open('C:\\Users\\chenj\\Desktop\\log.txt', 'r') as f:
                    log = f.readlines()[-1]
                    logstr = log.split()
                    date_begin = logstr[0]
                    date_end = logstr[1]
                    pageNum = int(logstr[2])
                find_a_year(url, referer, date_begin, date_end, pageNum, keyWord)
                if count > 0:
                    time_seg /= 2
                count = 0
        except:
            print("429 Error")
            count += 1
            time_seg += time_del
            with open('C:\\Users\\chenj\\Desktop\\log.txt', 'a') as f:
                f.write(date_begin + ' ' + date_end + ' ' + str(pageError) + '\n')

