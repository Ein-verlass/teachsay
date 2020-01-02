<%@ WebHandler Language = "C#"  Class="yanzhengma" %>
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Windows;
//需要添加的引用
using System.Drawing;
using System.Drawing.Drawing2D;//二维的图形或图像
using System.Web.SessionState;
 
namespace NewSystem.handler
{
    /// <summary>

    /// </summary>
    public class yanzhengma : IHttpHandler, IRequiresSessionState
    //要使用session必须实现该接口
    {
 
        public void ProcessRequest(HttpContext context)
        {
            //产生5位随机字符
            string checkCode = GenCode(5);
            //将字符串保存到session中，以便需要时进行验证
            context.Session["Code"] = checkCode;
            //产生宽70，高22的位图
            System.Drawing.Bitmap image = new System.Drawing.Bitmap(70, 22);
            //从指定的image（容器，用户装载图画）中创建新的Graphics
            //（工具，用于操作图画）
            Graphics g = Graphics.FromImage(image);
 
            try
            {
                //生成随机生成器
                Random random = new Random();
 
                //清空图片背景色
                g.Clear(Color.White);
 
                //画图片的背景噪音线
                int i;
                for (i = 0; i < 25; i++)
                {
                    int x1 = random.Next(image.Width);
                    int x2 = random.Next(image.Width);
                    int y1 = random.Next(image.Width);
                    int y2 = random.Next(image.Width);
 
                    g.DrawLine(new Pen(Color.Silver), x1, y1, x2, y2);
 
                }
 
                //设置字体样式
                Font font = new System.Drawing.Font("Arial", 12, (System.Drawing.FontStyle.Bold));
                System.Drawing.Drawing2D.LinearGradientBrush
                brush = new System.Drawing.Drawing2D.LinearGradientBrush(
               new Rectangle(0, 0, image.Width, image.Height), Color.Blue, Color.DarkRed,
               1.2F, true);
 
                //文本字符串格式，字体样式,文本样式，文本起始左上角x,y
 
                g.DrawString(checkCode, font, brush, 2, 2);
 
                g.DrawString(checkCode, font, brush, 2, 2);//文本字符串格式，字体样式,文本样式，文本起始左上角x,y
 
                //画图片的前景噪音点
                g.DrawRectangle(new Pen(Color.Silver), 0, 0, image.Width - 1, image.Height - 1);
                System.IO.MemoryStream ms = new System.IO.MemoryStream();//声明一个类对象，读写内存不是磁盘，
                image.Save(ms, System.Drawing.Imaging.ImageFormat.Gif);//指定的文件，指定的格式，图像格式
                context.Response.ClearContent();//清楚缓冲区流的所有内容输出
                context.Response.ContentType = "image/Gif";
                context.Response.BinaryWrite(ms.ToArray());//将一个二进制字符串写入HTTP流中(将流内容写入字符数组)
            }
            finally
            {
                g.Dispose();//释放资源
                image.Dispose();//释放image占用的资源
            }
        }
 
        public bool IsReusable
        {
            get
            {
                return false;
            }
        }
 
        /// <summary>
        /// 产生随机字符串
        /// </summary>
        /// <param name="num">随机出几个字符</param>
        /// <returns>随机出的字符串</returns>
        private string GenCode(int num)
        {
            string str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";            
            char[] chastr = str.ToCharArray();
            string code = "";
            Random rd = new Random();
            int i;
            for (i = 0; i < num; i++)
            {
                //产生随机截取位置
                code += str.Substring(rd.Next(0, str.Length), 1);
 
            }
 
            return code;
        }
    }
 
 
}