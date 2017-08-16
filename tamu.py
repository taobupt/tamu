import requests
from bs4 import BeautifulSoup

class Tamu():
    def __init__(self):
        self.headers=None
    def print_text_file(self,text):
        with open('/Users/tao/Desktop/untitled.html','wt')as f:
            f.write(text)



    def cas_login(self,NetID,password):
        URL='https://cas.tamu.edu/cas/login'
        client = requests.session()
        x = client.get(URL)
        self.headers = {
        'Origin': 'https://cas.tamu.edu',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Referer': 'https://cas.tamu.edu/cas/login?service=https://howdy.tamu.edu/uPortal/Login&renew=true',
        'Connection': 'keep-alive',
        }

        data = {'csrfmiddlewaretoken': 'AVEogidzmt8mdHkfpB9miioFFgyGoJ6K', 'username': NetID, 'password': password, 'lt': 'LT-fdzSgU9v2cPNyFaxwMHCjr1pGeZqklQV-cas-node-1', '_eventId': 'submit'}
        params = (
            ('service', 'https://howdy.tamu.edu/uPortal/Login'),
            ('renew', 'true'),
        )
        data['csrfmiddlewaretoken']=x.cookies['csrftoken']
        x = client.post(URL,headers=self.headers,data=data,params=params)
        #self.print_text_file(x.text)
        soup = BeautifulSoup(x.text, 'html.parser')
        error = soup.find('p',{'class':'alert__title'})
        if error is not None:
            error = error.text
        return error,client

    def get_term_list(self):
        error,client = self.cas_login()
        self.headers={
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'https://howdy.tamu.edu/uPortal/f/my-record/normal/render.uP',
            'Connection': 'keep-alive',
        }
        xx= client.get('https://howdy.tamu.edu/uPortal/p/TAMU-APP-Launcher/detached/render.uP?targetEndpoint=bwykfcls.p_sel_crse_search', headers=self.headers)
        #print(xx.cookies)
        #self.print_text_file(xx.text)

        self.headers={
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'https://howdy.tamu.edu/uPortal/f/my-record/normal/render.uP',
            'Connection': 'keep-alive',
        }
        xx=client.get('https://howdy.tamu.edu/uPortal/p/TAMU-APP-Launcher.ctf3/detached/render.uP?pCm=view&pP_targetEndpoint=bwykfcls.p_sel_crse_search',headers=self.headers)
        #print(xx.cookies)
        #self.print_text_file(xx.text)



        self.headers= {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'https://howdy.tamu.edu/uPortal/p/TAMU-APP-Launcher.ctf3/detached/render.uP?pCm=view&pP_targetEndpoint=bwykfcls.p_sel_crse_search',
            'Connection': 'keep-alive',
        }
        xx=client.get('https://compass-sso.tamu.edu/ssomanager/c/SSB?pkg=bwykfcls.p_sel_crse_search', headers=self.headers)
        #print(xx.cookies)
        #self.print_text_file(xx.text)

        data = [
            ('p_calling_proc', 'P_CrseSearch'),
            ('p_term', '201731'),
        ]
        self.headers={
            'Origin': 'https://compass-ssb.tamu.edu',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'Referer': 'https://compass-ssb.tamu.edu/pls/PROD/bwykfcls.p_sel_crse_search',
            'Connection': 'keep-alive',
        }
        xx=client.post('https://compass-ssb.tamu.edu/pls/PROD/bwykgens.p_proc_term_date?deviceType=C', headers=self.headers,
                      cookies=xx.cookies, data=data)

        #print(xx.cookies)
        #self.print_text_file(xx.text)


        self.headers = {
            'Origin': 'https://compass-ssb.tamu.edu',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'Referer': 'https://compass-ssb.tamu.edu/pls/PROD/bwykgens.p_proc_term_date?deviceType=C',
            'Connection': 'keep-alive',
        }
        data = [
            ('rsts', 'dummy'),
            ('crn', 'dummy'),
            ('term_in', '201731'),
            ('sel_subj', 'dummy'),
            ('sel_subj', 'CSCE'),
            ('sel_day', 'dummy'),
            ('sel_schd', 'dummy'),
            ('sel_insm', 'dummy'),
            ('sel_camp', 'dummy'),
            ('sel_levl', 'dummy'),
            ('sel_sess', 'dummy'),
            ('sel_instr', 'dummy'),
            ('sel_ptrm', 'dummy'),
            ('sel_ptrm', '%'),
            ('sel_attr', 'dummy'),
            ('sel_crse', ''),
            ('sel_title', ''),
            ('sel_from_cred', ''),
            ('sel_to_cred', ''),
            ('begin_hh', '0'),
            ('begin_mi', '0'),
            ('begin_ap', 'x'),
            ('end_hh', '0'),
            ('end_mi', '0'),
            ('end_ap', 'x'),
            ('path', '1'),
            ('SUB_BTN', 'Course Search'),
        ]
        xx = client.post('https://compass-ssb.tamu.edu/pls/PROD/bwykfcls.P_GetCrse?deviceType=C', headers=self.headers, cookies=xx.cookies, data=data)
        #print(xx.cookies)
        #self.print_text_file(xx.text)

        courses = self.parse_course(xx.text)

        self.headers={
            'Origin': 'https://compass-ssb.tamu.edu',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'Referer': 'https://compass-ssb.tamu.edu/pls/PROD/bwykfcls.P_GetCrse?deviceType=C',
            'Connection': 'keep-alive',
        }

        data = [
            ('term_in', '201731'),
            ('sel_subj', 'dummy'),
            ('sel_subj', 'CSCE'),
            ('SEL_CRSE', '221'),
            ('SEL_TITLE', ''),
            ('BEGIN_HH', '0'),
            ('BEGIN_MI', '0'),
            ('BEGIN_AP', 'a'),
            ('SEL_DAY', 'dummy'),
            ('SEL_PTRM', 'dummy'),
            ('END_HH', '0'),
            ('END_MI', '0'),
            ('END_AP', 'a'),
            ('SEL_CAMP', 'dummy'),
            ('SEL_SCHD', 'dummy'),
            ('SEL_SESS', 'dummy'),
            ('SEL_INSTR', 'dummy'),
            ('SEL_INSTR', '%'),
            ('SEL_ATTR', 'dummy'),
            ('SEL_ATTR', '%'),
            ('SEL_LEVL', 'dummy'),
            ('SEL_LEVL', '%'),
            ('SEL_INSM', 'dummy'),
            ('sel_dunt_code', ''),
            ('sel_dunt_unit', ''),
            ('call_value_in', 'BASIC'),
            ('rsts', 'dummy'),
            ('crn', 'dummy'),
            ('path', '1'),
            ('SUB_BTN', 'View Sections'),
        ]
        cookies = xx.cookies
        for course in courses:
            data[3]=('SEL_CRSE',course)
            xx=client.post('https://compass-ssb.tamu.edu/pls/PROD/bwykfcls.P_GetCrse?deviceType=C', headers=self.headers, cookies=cookies, data=data)
            #print(xx.cookies)
            #self.print_text_file(xx.text)
            self.parse_html(xx.text)
    def parse_course(self,location):
        soup = BeautifulSoup(location,'html.parser')
        value = soup.find_all('input',{'name':'SEL_CRSE'})
        courses=[]
        for val in value:
            courses.append(val.get('value'))
        print(courses)
        return courses

    def parse_table(self,row,tag):
        cols = row.find_all(tag)
        cols = [ele.text.strip() for ele in cols]
        return [ele for ele in cols if ele]

    def parse_html(self,location):
        soup = BeautifulSoup(location,'html.parser')
        table = soup.find('table',attrs={'class','datadisplaytable'})
        rows = table.find_all('tr')
        data=[]
        for row in rows:
            data.append(self.parse_table(row,'th'))
            data.append(self.parse_table(row,'td'))
        data=[x for x in data if x]
        min_len = min(len(data[1]),len(data[2]))
        dic={}
        for ind in range(0,min_len):
            dic[data[1][ind]]=data[2][ind]
        print(dic)
