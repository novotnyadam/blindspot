# -*- coding: utf-8 -*-

import pandas as pd

def parse_file(txt):
    """
    Parses the .txt file into pandas DataFrame with columns rewritten from .txt file
    :input: .txt file
    :output: pd.DataFrame
    """
    
    file = open(txt)
    lines = file.readlines()
    chunks = []
    # parse file into chunks of beginning with either GET, POST or PUT
    for idx, line in enumerate(lines):
        chunk = []
        if line.startswith("GET"):
            chunk = lines[idx:idx+11]
            chunks.append(chunk)
        elif line.startswith("POST") or line.startswith("PUT"):
            chunk = lines[idx:idx+15]
            chunks.append(chunk)
                        
    # parse chunks into pd.DataFrame; getting rid of column name and redundant '\n' in the process
    header = ["Method", "URL", "Protocol", "UserAgent", "Pragma", "CacheControl", "Accept", "AcceptEncoding", 
              "AcceptCharset", "AcceptLanguage", "Host", "Cookie", "Connection", 
              "ContentType", "ContentLength", "Payload"]    
    data = []
    for chunk in chunks:
        if chunk[0].split()[0] == "GET":
            row = {
                header[0]: chunk[0].split()[0], #method
                header[1]: chunk[0].split()[1], #url
                header[2]: chunk[0].split()[2], #protocol
                header[3]: chunk[1].replace('User-Agent: ', '').replace('\n', ''), #user-agent
                header[4]: chunk[2].replace('Pragma: ', '').replace('\n', ''), #pragma
                header[5]: chunk[3].replace('Cache-control: ', '').replace('\n', ''), #cache-control
                header[6]: chunk[4].replace('Accept: ', '').replace('\n', ''), #accept
                header[7]: chunk[5].replace('Accept-Encoding: ', '').replace('\n', ''), #accept-encoding
                header[8]: chunk[6].replace('Accept-Charset: ', '').replace('\n', ''), #accept-charset
                header[9]: chunk[7].replace('Accept-Language: ', '').replace('\n', ''), #accept-language
                header[10]: chunk[8].replace('Host: ', '').replace('\n', ''), #host 
                header[11]: chunk[9].replace('Cookie: ', '').replace('\n', ''), #cookie
                header[12]: chunk[10].replace('Connection: ', '').replace('\n', ''), #connection
                header[13]: '', #content-type
                header[14]: 0, #content-length
                header[15]: ''  #payload
            }
            data.append(row)
        if chunk[0].split()[0] == "POST" or chunk[0].split()[0] == "PUT":
            row = {
                header[0]: chunk[0].split()[0], #method
                header[1]: chunk[0].split()[1], #url
                header[2]: chunk[0].split()[2], #protocol
                header[3]: chunk[1].replace('User-Agent: ', '').replace('\n', ''), #user-agent
                header[4]: chunk[2].replace('Pragma: ', '').replace('\n', ''), #pragma
                header[5]: chunk[3].replace('Cache-control: ', '').replace('\n', ''), #cache-control
                header[6]: chunk[4].replace('Accept: ', '').replace('\n', ''), #accept
                header[7]: chunk[5].replace('Accept-Encoding: ', '').replace('\n', ''), #accept-encoding
                header[8]: chunk[6].replace('Accept-Charset: ', '').replace('\n', ''), #accept-charset
                header[9]: chunk[7].replace('Accept-Language: ', '').replace('\n', ''), #accept-language
                header[10]: chunk[8].replace('Host: ', '').replace('\n', ''), #host 
                header[11]: chunk[9].replace('Cookie: ', '').replace('\n', ''), #cookie
                header[13]: chunk[10].replace('Content-Type: ', '').replace('\n', ''), #content-type
                header[12]: chunk[11].replace('Connection: ', '').replace('\n', ''), #connection
                header[14]: int(chunk[12].replace('Content-Length: ', '')), #content-length
                header[15]: chunk[14], #payload
            }
            data.append(row)
    data = pd.DataFrame(data, columns = header)
    file.close()
    return data
    