import requests,re,sys,urllib.parse,os,pickle

#SETTINGS
url = '' #https://example.com
usr=''
pwd=''
proxies = {}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
verify=True
ffmpeg_path='' #C:\\example\\ffmpeg
video_dir='videos\\'
links_file='videos\\links_pickle'
if not (os.path.isdir(video_dir)):
    os.mkdir(video_dir)
#####################################

s=requests.session()

def extract_values(regex,url,name,critical):
    r = s.get(url, headers=headers, proxies=proxies, verify=verify)
    value = re.findall(regex,r.text)
    if len(value)>0:
        if critical:
            print('[+] ' + name + ' extracted: ' + value[0])
        return value
    else:
        if critical:
            print('[-] ' + name + ' error!')
            sys.exit(1)
        else:
            return value

def login():
    print('[+] Logging in...')
    logintoken = extract_values('logintoken" value="(.*?)"',url+'/login/index.php','Login token',True)[0]
    data={
            'anchor':'',
            'logintoken':logintoken,
            'username':usr,
            'password':pwd
            }
    r = s.post(url+'/login/index.php', data=data, headers=headers, proxies=proxies, verify=verify)
    if r.url == url+'/my/':
        print('[+] Login successful!')
    else: 
        print('[-] Login failure!')
        sys.exit(1)
        
def get_subjects():
    print('[+] Getting sesskey...')
    sesskey = extract_values('"sesskey":"(.*?)"',url+'/my/','Sesskey',True)[0]
    data='[{"index":0,"methodname":"core_course_get_enrolled_courses_by_timeline_classification","args":{"offset":0,"limit":0,"classification":"all","sort":"fullname","customfieldname":"","customfieldvalue":""}}]'
    r = s.post(url+'/lib/ajax/service.php?sesskey='+sesskey+'&info=core_course_get_enrolled_courses_by_timeline_classification', data=data,headers=headers, proxies=proxies, verify=verify).json()
    subjects = r[0]['data']['courses']
    return subjects
    
def erase_polish_chars(input_string):
    output_string=input_string.replace('Ą','A').replace('ą','a')
    output_string=output_string.replace('Ć','C').replace('ć','c')
    output_string=output_string.replace('Ę','E').replace('ę','e')
    output_string=output_string.replace('Ł','L').replace('ł','l')
    output_string=output_string.replace('Ń','N').replace('ń','n')
    output_string=output_string.replace('Ó','O').replace('ó','o')
    output_string=output_string.replace('Ś','S').replace('ś','s')
    output_string=output_string.replace('Ź','Z').replace('ź','z')
    output_string=output_string.replace('Ż','Z').replace('ż','z')
    return output_string    

def get_links(subjects):
    links=[]
    #SUBJECTS
    for subject in subjects:
        conferences = extract_values('href="(https://[^"]*/bigbluebuttonbn/[^"]*)"',subject['viewurl'],'Conferences',False)
        print('{} ({})'.format(subject['shortname'],subject['viewurl']))
        #CONFERENCES
        conference_count=0
        for conference_link in conferences:
            conference_count+=1
            print('\t' + conference_link)
            bbb_links = extract_values('href=(https[^"]*meetingId[^"]*)"',conference_link,'Bbb links',False)
            #BBB LINKS
            i=0
            for bbb_link in bbb_links:
                i+=1
                link = urllib.parse.unquote(bbb_link)
                conference_suffix=''
                if conference_count>1:
                    conference_suffix=str(conference_count)
                print('\t\t' + link)
                url = re.findall('https://[^/]*/',link)[0]
                meeting_id = re.findall('meetingId=(.*)$',link)[0]
                webcams_url = url+'presentation/'+meeting_id+'/video/webcams.webm'
                deskshare_url = url+'presentation/'+meeting_id+'/deskshare/deskshare.webm'
                webcams_filename = erase_polish_chars(subject['shortname'].replace(' ','_')+ conference_suffix + '_' + str(i) +'_webcams.webm')
                deskshare_filename = erase_polish_chars(subject['shortname'].replace(' ','_')+ conference_suffix + '_' + str(i) + '_deskshare.webm')
                output_filename = erase_polish_chars(subject['shortname'].replace(' ','_')+ conference_suffix + '_' + str(i) + '.mp4')
                print('\t\t\t{}'.format(webcams_url))
                print('\t\t\t{}'.format(deskshare_url))
                links.append((webcams_filename,webcams_url,deskshare_filename,deskshare_url,output_filename))
        print()
    print('[+] Links extracted!')
    print('#######################')
    with open(links_file, 'wb') as f:
        pickle.dump(links, f)
    return links
    
def save_videos(links,path):
    i=0
    print('[+] Downloading videos')
    for link in links:
        i+=1
        if not os.path.isfile(path+link[2]) or not os.path.isfile(path+link[0]):
            print('{}/{}'.format(i,len(links)))
        if not os.path.isfile(path+link[0]):
            r = s.get(link[1], headers=headers, proxies=proxies, verify=verify) 
            with open(path+link[0], 'wb') as f:
                f.write(r.content)
        if not os.path.isfile(path+link[2]):
            r = s.get(link[3], headers=headers, proxies=proxies, verify=verify) 
            with open(path+link[2], 'wb') as f:
                f.write(r.content)

def convert_videos(links,path):
    print('[+] Converting videos')
    for link in links:
            if not os.path.isfile(path+link[4]):
                cmd='{} -i "{}{}" -i "{}{}" -c copy "{}{}"'.format(ffmpeg_path,path,link[2],path,link[0],path,link[4])
                print(cmd)
                os.system(cmd)

def remove_webms(links,path):
    print('[+] Erasing webms')
    for link in links:
        if os.path.isfile(path+link[2]):
            os.remove(path+link[2]) 
        if os.path.isfile(path+link[0]):
            os.remove(path+link[0]) 

#####################################
links=[]
login()
if os.path.isfile(links_file):
    with open(links_file, 'rb') as f:
        links =  pickle.load(f)
    print('[+] Links loaded!')
else:
    subjects = get_subjects()
    links = get_links(subjects)
    save_videos(links,video_dir)
convert_videos(links,video_dir)
remove_webms(links,video_dir)
