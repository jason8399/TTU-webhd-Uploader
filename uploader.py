from requests import Request, Session


class Uploader:

    def __init__(self):
        self.__s = Session()
        self.__header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.10 Safari/537.36"}
        self.__url = "http://webhd1.ttu.edu.tw/"
        self.__index = "index.php"
        self.__main = "main/"
        self.__showhd = "showhd.php"
        self.__upload = "upload.php"
        sefl.__sharefile = "sharefile.php"
        self.__login_data = {"ID": "", "PWD": "", "Submit": "登入"}
        self.__upload_form = {"GoUpload": "1",
                              "MAX_FILE_SIZE": "102400000",
                              "fname1": "",
                              "fname2": "",
                              "fname3": "",
                              "fname4": "",
                              "orgfn1": "",
                              "orgfn2": "",
                              "orgfn3": "",
                              "orgfn4": ""
                              }

        self.__file_path = "C:\\fakepath\\"
        self.__file_name = ""
        self.__files = {"userfile1": "", "userfile2": "", "userfile3": "", "userfile4": ""}
        self.__share_form = {"fname": "", "idname": "", "ShareKey": "", "Confirm": "確認送出"}
        self.__share_idname = ""
        self.__s.headers.update(headers)

    def login(self):
        self.__response = self.__s.get(self.__url + self.__index)
        self.__login_data["ID"] = ""
        self.__login_data["PWD"] = ""
        self.__response = self.__s.post(self.__url + self.__index, data=self.__login_data)

    def upload(self):
        self.__response = self.__s.get(self.__url + self.__main + self.__showhd, params={"Action": "Upload"})
        self.__upload_form["fname1"] = file_name
        self.__upload_form["orgfin1"] = file_path + file_name
        self.__files["userfile1"] = open(file_name, "rb")
        self.__response = self.__s.post(self.__url + self.__main + self.__upload, data=self.__upload_form, files=self.__files)

    def share(self):
        self.__response = self.__s.get(self.__url + self.__main + self.__showhd, params={"Action": "ShareFile", "fname": self.__file_name})
        self.__share_form["fname"] = self.__file_name
        self.__share_form["idname"] = self.__share_idname
        self.__response = self.__s.post(self.__url + self.__main + self.__sharefile, data=self.__share_form)
