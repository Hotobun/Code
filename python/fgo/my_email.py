import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
 
my_sender='hotobun@163.com'    # 发件人邮箱账号
my_pass = 'hotococoa15'              # 发件人邮箱密码
my_user='hotococoa@qq.com'      # 收件人邮箱账号，我这边发送给自己

image_path = r'C:\Users\Hoto\Pictures\Saved Pictures\捕获3.PNG'

def mail():

    message = MIMEMultipart()
    msg=MIMEText('title','plain','utf-8')
    msg['From']=formataddr(["FromRunoob",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To']=formataddr(["FK",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject']="发送邮件测试"                # 邮件的主题，也可以说是标题

    message.attach(msg)

    with open(image_path, 'rb') as f:
        mime = MIMEBase('image','jpeg',filename='1.jpg')
        mime.add_header('Content-Disposition', 'attachment', filename='1.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        message.attach(mime)
        print ('message.attack complate')
    att = MIMEText(open(image_path, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="1.jpg"'
    message.attach(att)
    print ('2  complate')


    server=smtplib.SMTP_SSL("smtp.163.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
    server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接
    print("邮件发送成功")

def send(img_path,sender = 'hotococoa@qq.com' , receivers = 'hotococoa@qq.com'):
    message =  MIMEMultipart()
    subject = '终于能发图片了'
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receivers
    content = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>good!','html','utf-8')  
    message.attach(content)

    file=open(img_path, "rb")
    img_data = file.read()
    file.close()

    img = MIMEImage(img_data)
    img.add_header('Content-ID', '<image1>')
    message.attach(img)

    server=smtplib.SMTP_SSL("smtp.qq.com")  # 发件人邮箱中的SMTP服务器，端口是25
    server.login(sender,'xczznzqpldtbbjjh')  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(sender,receivers,message.as_string())   # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()
    print ("邮件发送成功")
        


if __name__ == "__main__":
    send(image_path)
