
import pickle


import base64
import json
import time
import email
from bs4 import BeautifulSoup
from pprint import pprint
def main():

	body = {'headers': ['Received: by mx0054p1mdw1.sendgrid.net with SMTP id w1U6fwkKjV Fri, 24 Jul 2020 15:47:26 +0000 (UTC)\nReceived: from mail-qt1-f173.google.com (mail-qt1-f173.google.com [209.85.160.173]) by mx0054p1mdw1.sendgrid.net (Postfix) with ESMTPS id EFC2E6E1AA9 for <something@project-m.app>; Fri, 24 Jul 2020 15:47:25 +0000 (UTC)\nReceived: by mail-qt1-f173.google.com with SMTP id e7so7228882qti.1 for <something@project-m.app>; Fri, 24 Jul 2020 08:47:25 -0700 (PDT)\nDKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=hawkmail.newpaltz.edu; s=google; h=mime-version:date:from:subject:thread-topic:message-id:to :content-transfer-encoding; bh=Du381n3UAAbskEX4cyA6Te8XVALacWpL5JFbopbrrw4=; b=j6vDSyBX4JJAvunWcFW5B2YBB56KEkZrRfH77IuKp4b16AU8CmT8fBIaRLqxStXFEB emFEhB85WIuN+fMPvC13GPfNpRQEQXAoFa6evJ2yOk4il2PHV6X+Vugr5dlvCoeO/w8S HndNbWa958LMdwZYdJpAI8YRt0Mfb4+vRXgyw=\nX-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=1e100.net; s=20161025; h=x-gm-message-state:mime-version:date:from:subject:thread-topic :message-id:to:content-transfer-encoding; bh=Du381n3UAAbskEX4cyA6Te8XVALacWpL5JFbopbrrw4=; b=N3pkVfzpw/q6T2cHRz2lUUuW8HhFLMRL7ihltOs2fSrrsAOJNAqZlLTfja4DLQx5lW mt0gL5KBIH4C4Wh5zcmxXQAVmwd1dV2XULJl2+f9hahJxCr15EIQvRCHfDDXTaDnyrYU CFIb2r8PyPlamc4u7R3c5PFU8evAbmYSqiKSW6FaactvM+SyVk0QEOlc2QOT+xz7WHCi rjJWPoF6sGkbJC9IegchmXh/iNS/bXhD9yTQk0l69zMl/MbLyFYb4hPhlUDLyQkMoxRB uNu4EZMe04h6eSrhrHPZbrWZEd01O+wpcaTFsv4IHe1FGHVOILqmS/wyMNasp7k6HMmq 7qOw==\nX-Gm-Message-State: AOAM531i1Lrrr/WmX+O2f9f6cIyBl8jwFV4VPxjVM+osQu/HTgxq+K5D KV0wpZnYdHWtWoQf4w3f/IUpkIfNCQA=\nX-Google-Smtp-Source: ABdhPJyc7r9tUmtLNWUBk/MDGzAV/ciukCPTxMrSUh0bURoj5hhV1KH7OJ21xJ6JKWiq16NvTCJAUQ==\nX-Received: by 2002:ac8:6d2f:: with SMTP id r15mr10149263qtu.281.1595605644992; Fri, 24 Jul 2020 08:47:24 -0700 (PDT)\nReceived: from smtp.gmail.com (pool-98-113-195-211.nycmny.fios.verizon.net. [98.113.195.211]) by smtp.gmail.com with ESMTPSA id c7sm1922902qta.95.2020.07.24.08.47.23 for <something@project-m.app> (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-GCM-SHA256 bits=128/128); Fri, 24 Jul 2020 08:47:24 -0700 (PDT)\nMIME-Version: 1.0\nDate: Fri, 24 Jul 2020 11:47:21 -0400\nFrom: Pharez Varlack <varlackp1@hawkmail.newpaltz.edu>\nSubject: Thanks sendgrid\nThread-Topic: Thanks sendgrid\nMessage-ID: <438A6D2B-9911-4ADB-8DCA-FF7BF28878CA@hxcore.ol>\nTo: "something@project-m.app" <something@project-m.app>\nContent-Transfer-Encoding: quoted-printable\nContent-Type: text/html; charset="utf-8"\n'], 'dkim': ['{@hawkmail.newpaltz.edu : pass}'], 'to': ['"something@project-m.app" <something@project-m.app>'], 'html': ['<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns:m="http://schemas.microsoft.com/office/2004/12/omml" xmlns="http://www.w3.org/TR/REC-html40"><head><meta http-equiv=Content-Type content="text/html; charset=utf-8"><meta name=Generator content="Microsoft Word 15 (filtered medium)"><style><!--\n/* Font Definitions */\n@font-face\n\t{font-family:"Cambria Math";\n\tpanose-1:2 4 5 3 5 4 6 3 2 4;}\n@font-face\n\t{font-family:Calibri;\n\tpanose-1:2 15 5 2 2 2 4 3 2 4;}\n/* Style Definitions */\np.MsoNormal, li.MsoNormal, div.MsoNormal\n\t{margin:0in;\n\tmargin-bottom:.0001pt;\n\tfont-size:11.0pt;\n\tfont-family:"Calibri",sans-serif;}\n.MsoChpDefault\n\t{mso-style-type:export-only;}\n@page WordSection1\n\t{size:8.5in 11.0in;\n\tmargin:1.0in 1.0in 1.0in 1.0in;}\ndiv.WordSection1\n\t{page:WordSection1;}\n--></style></head><body lang=EN-US><div class=WordSection1><p class=MsoNormal><o:p>&nbsp;</o:p></p><p class=MsoNormal>At least better than google</p><p class=MsoNormal>Best,<o:p></o:p></p><p class=MsoNormal>Pharez J. Varlack<o:p></o:p></p><p class=MsoNormal><o:p>&nbsp;</o:p></p></div></body></html>\n'], 'from': ['Pharez Varlack <varlackp1@hawkmail.newpaltz.edu>'], 'sender_ip': ['209.85.160.173'], 'spam_report': ['Spam detection software, running on the system "mx0054p1mdw1.sendgrid.net", has\nidentified this incoming email as possible spam.  The original message\nhas been attached to this so you can view it (if it isn\'t spam) or label\nsimilar future email.  If you have any questions, see\n@@CONTACT_ADDRESS@@ for details.\n\nContent preview:  At least better than google Best, Pharez J. Varlack [...] \n\nContent analysis details:   (1.1 points, 5.0 required)\n\n pts rule name              description\n---- ---------------------- --------------------------------------------------\n 0.0 HTML_MESSAGE           BODY: HTML included in message\n 1.1 MIME_HTML_ONLY         BODY: Message only has text/html MIME parts\n\n'], 'envelope': ['{"to":["something@project-m.app"],"from":"varlackp1@hawkmail.newpaltz.edu"}'], 'attachments': ['0'], 'subject': ['Thanks sendgrid'], 'spam_score': ['1.106'], 'charsets': ['{"to":"UTF-8","html":"utf-8","subject":"UTF-8","from":"UTF-8"}'], 'SPF': ['pass']}
	subject = body['subject']
	html = body['html']
	pprint(json.loads(body['envelope'][0])['from'])
	sender = body['from']
	print(sender)
	#print(type(html))
	#html_parsed = BeautifulSoup(html[0], 'html.parser')
	#print(html_parsed.text)
	#print(subject, sender, "\n\n", html)		

# TODO
# automate calling the pubSub to watch the email address once a week
# create users in our database
# url validation server side
main()
