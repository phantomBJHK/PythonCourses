< !DOCTYPE
html >
< html


class ="nx-main980" >

< head >
< meta
content = "text/html; charset=utf-8"
http - equiv = "Content-Type" / >
< meta
content = "IE=EmulateIE8"
http - equiv = "X-UA-Compatible" / >
< meta
content = "人人网 校内是一个真实的社交网络，联络你和你周围的朋友。 加入人人网校内你可以:联络朋友，了解他们的最新动态；和朋友分享相片、音乐和电影；找到老同学，结识新朋友；用照片和日志记录生活,展示自我。"
name = "Description" / >
< meta
content = "Xiaonei,Renren,校内,大学,同学,同事,白领,个人主页,博客,相册,群组,社区,交友,聊天,音乐,视频,校园,人人,人人网"
name = "Keywords" / >
< meta
content = "232517306762562566375"
property = "qc:admins" / >
< meta
content = "f2fdc876b8ba2a5d"
property = "wb:webmaster" / >
< meta
content = "App"
name = "msApplication-ID" / >
< meta
content = "57722RenRenpreview.RenrenHD_fknrsfzqca1jw"
name = "msApplication-PackageFamilyName" / > < link
href = "http://a.xnimg.cn/favicon-rr.ico?ver=3"
rel = "shortcut icon"
type = "image/x-icon" / >
< link
href = "http://a.xnimg.cn/wap/apple_icon_.png"
rel = "apple-touch-icon" / >
< script
type = "text/javascript" >
XN = {get_check: '', get_check_x: '35d578c9', env: {domain: 'renren.com', shortSiteName: '人人', siteName: '人人网'}};
try {
window.onerror=function(){
var a=arguments, e=encodeURIComponent, l=location, d=new Date();
if (a.length != 3 | | a[2] == 0)
return 1;
new
Image().src = ['http://s.renren.com/speedstats/jserror/stats.php?message=' + e(a[0]),
               'url=' + e(a[1]), 'lineNo=' + a[2], 'location=' + e(l), 'time=' + d.toLocaleTimeString()].join('&');
return 1;
};
} catch(e)
{};
< / script > < meta
charset = "utf-8" / >
          < link
href = "http://a.xnimg.cn/favicon-rr.ico?ver=3"
rel = "shortcut icon"
type = "image/x-icon" / >
       < link
href = "http://a.xnimg.cn/wap/apple_icon_.png"
rel = "apple-touch-icon" / >
      < link
href = "http://s.xnimg.cn/a86614/nx/core/base.css"
rel = "stylesheet"
type = "text/css" / >
       < script
type = "text/javascript" >
if (typeof nx == = 'undefined')
{
    var
nx = {};
}
nx.log = {
    startTime: + new Date()
};
nx.user = {
    id: "",
    ruid: "",
    tinyPic: " ",
    name: "",
    privacy: "",
    requestToken: '',
    _rtk: '35d578c9'
};
nx.user.isvip = false;
nx.user.hidead = false;
nx.webpager = nx.webpager | | {};
nx.production = true;
< / script >
    < script
src = "http://s.xnimg.cn/a83151/nx/core/libs.js"
type = "text/javascript" > < / script >
                               < script
type = "text/javascript" > \
       define.config({map: {
           "backbone": "http://s.xnimg.cn/a75208/nx/core/backbone.js",
           "ui/draggable": "http://s.xnimg.cn/a70750/nx/core/ui/draggable.js",
           "ui/menu": "http://s.xnimg.cn/a70736/nx/core/ui/menu.js",
           "ui/resizable": "http://s.xnimg.cn/a70738/nx/core/ui/resizable.js",
           "ui/sortable": "http://s.xnimg.cn/a70749/nx/core/ui/sortable.js",
           "ui/tabs": "http://s.xnimg.cn/a78333/nx/core/ui/tabs.js",
           "ui/ceiling": "http://s.xnimg.cn/a76297/nx/core/ui/ceiling.js",
           "ui/columns": "http://s.xnimg.cn/a68070/nx/core/ui/columns.js",
           "ui/dialog": "http://s.xnimg.cn/a76395/nx/core/ui/dialog.js",
           "ui/fileupload": "http://s.xnimg.cn/a81310/nx/core/ui/fileupload.js",
           "ui/pagination": "http://s.xnimg.cn/a70307/nx/core/ui/pagination.js",
           "ui/placeholder": "http://s.xnimg.cn/a79685/nx/core/ui/placeholder.js",
           "ui/progressbar": "http://s.xnimg.cn/a62964/nx/core/ui/progressbar.js",
           "ui/rows": "http://s.xnimg.cn/a62964/nx/core/ui/rows.js",
           "ui/scroll": "http://s.xnimg.cn/a61518/nx/core/ui/scroll.js",
           "ui/scrollbar": "http://s.xnimg.cn/a76868/nx/core/ui/scrollbar.js",
           "ui/select": "http://s.xnimg.cn/a82096/nx/core/ui/select.js",
           "ui/slideshow": "http://s.xnimg.cn/a72804/nx/core/ui/slideshow.js",
           "ui/speech": "http://s.xnimg.cn/a77631/nx/core/ui/speech.js",
           "ui/textbox": "http://s.xnimg.cn/a79526/nx/core/ui/textbox.js",
           "ui/renren/textbox": "http://s.xnimg.cn/a92727/nx/core/ui/renren/textbox.js",
           "ui/tooltip": "http://s.xnimg.cn/a73228/nx/core/ui/tooltip.js",
           "ui/renren/addfriend": "http://s.xnimg.cn/a78457/nx/core/ui/renren/addFriendLayer.js",
           "ui/renren/at": "http://s.xnimg.cn/a78409/nx/core/ui/renren/atAndEmotion.js",
           "ui/renren/emotion": "http://s.xnimg.cn/a78409/nx/core/ui/renren/atAndEmotion.js",
           "ui/renren/commentCenter": "http://s.xnimg.cn/a83569/nx/core/ui/renren/commentCenter.js",
           "ui/renren/friendgroup": "http://s.xnimg.cn/a62964/nx/core/ui/renren/friendGroup.js",
           "ui/renren/friendListSelector": "http://s.xnimg.cn/a78513/nx/core/ui/renren/friendListSelector.js",
           "ui/renren/like": "http://s.xnimg.cn/a83569/nx/core/ui/renren/like.js",
           "nx/namecard": "http://s.xnimg.cn/a77668/nx/core/ui/renren/namecard.js",
           "ui/renren/pagelayer": "http://s.xnimg.cn/a62964/nx/core/ui/renren/pageLayer.js",
           "ui/renren/photoupload": "http://s.xnimg.cn/a82833/nx/core/ui/renren/photoupload.js",
           "ui/renren/privacy": "http://s.xnimg.cn/a76680/nx/core/ui/renren/privacy.js",
           "ui/renren/share": "http://s.xnimg.cn/a78999/nx/core/ui/renren/share.js",
           "ui/renren/vocal": "http://s.xnimg.cn/a77347/nx/core/ui/renren/vocal.js",
           "ui/renren/mvideo": "http://s.xnimg.cn/a80641/nx/core/ui/renren/mvideo.js",
           "ui/renren/with": "http://s.xnimg.cn/a82994/nx/core/ui/renren/with.js",
           "ui/clipboard": "http://s.xnimg.cn/a63417/nx/core/ui/clipboard.js",
           "app/publisher": "http://s.xnimg.cn/a91505/nx/core/app/publisher.js",
           "viewer": "http://s.xnimg.cn/a83025/nx/photo/viewer/js/viewer.js",
           "media/player": "http://s.xnimg.cn/nx/photo/viewer/js/mediaplayer.js",
           "ui/renren/like/commentseed": "http://s.xnimg.cn/a64636/nx/core/ui/renren/like.seed.comment.js",
           "ui/renren/like/seed": "http://s.xnimg.cn/a62964/nx/core/ui/renren/like.seed.js",
           "ui/renren/share/seed": "http://s.xnimg.cn/a62964/nx/core/ui/renren/share.seed.js",
           "ui/renren/follow": "http://s.xnimg.cn/a78456/nx/core/ui/renren/follow.js",
           "ui/renren/relationFollow": "http://s.xnimg.cn/a78457/nx/core/ui/renren/relationFollow.js",
           "ui/autocomplete": "http://s.xnimg.cn/a70736/nx/core/ui/autocomplete.js",
           "ui/showCommonFriend": "http://s.xnimg.cn/a78917/nx/core/ui/renren/showcommonfriend.js",
           "photo/circler": "http://s.xnimg.cn/a73344/nx/photo/phototerminal/js/circler.js",
           "ui/friendSearch": "http://s.xnimg.cn/a64338/nx/core/ui/renren/friendSearch.js",
           "ui/renren/replyOption": "http://s.xnimg.cn/a68256/nx/core/ui/renren/replyOption.js",
           "photo/avatarUpload": "http://s.xnimg.cn/a77340/nx/photo/upload-avata/js/avatarUpload.js",
           "ui/renren/school": "http://s.xnimg.cn/a85689/nx/core/ui/renren/school.js"
       }});
nx.data.isDoubleFeed = Boolean();
nx.data.isDoubleFeedGuide = Boolean();
< / script >
    < script
src = "http://s.xnimg.cn/a95943/nx/core/base.js"
type = "text/javascript" > < / script >
                               <!--[ if lt
IE
9] >
< script
type = "text/javascript" > \
       document.execCommand("BackgroundImageCache", false, true);
< / script >
    <![endif] -->
< script
type = "text/javascript" > nx.webpager.disable = true; < / script >
                                                           < link
href = "login.css"
media = "all"
rel = "stylesheet"
type = "text/css" >
       < title > 人人网，中国领先的实名制SNS社交网络。加入人人网，找到老同学，结识新朋友。 < / title > < script
src = "http://s.xnimg.cn/a72842/n/core/base-all2.js"
type = "text/javascript" > < / script >
                               < / link > < / head >
                                              < body


class ="login" id="syshome" >

< div
id = "header" >
< div


class ="site-nav rr" id="navBar" >

< div


class ="navigation-wrapper" >

< div


class ="navigation navigation-new clearfix" >

< div
id = "logo2" >
< h1 >
< a
href = "http://www.renren.com"
title = "人人网 renren.com - 人人网校内是一个真实的社交网络，联系朋友，一起玩游戏" >
< img
alt = "人人网 renren.com - 人人网校内是一个真实的社交网络，联系朋友，一起玩游戏"
src = "http://a.xnimg.cn/nx/apps/login/cssimg/logo-big.jpg"
title = "人人网 renren.com - 人人网校内是一个真实的社交网络，联系朋友，一起玩游戏" / >
< / a >
< / h1 >
< / div >
< div


class ="nav-body clearfix" >

< div


class ="nav-other" >

< div


class ="menu" >

< a


class ="st-btn" href="http://st.renren.com" target="_blank" > 学生团体申请入口 < / a >

< / div >
< div


class ="menu" >

< a
href = "http://wwv.renren.com/xn.do?ss=10131&amp;rt=1&amp;g=v6reg"
id = "reg_link"
stats = "homenav_reg"
title = "注册" > 注册 < / a >
< / div >
< div


class ="menu" >

< a
href = "http://support.renren.com/link/suggest"
stats = "homenav_suggest"
title = "给我们提建议" > 反馈意见 < / a >
< / div >
< / div >
< / div >
< / div >
< / div >
< / div >
< / div >
< div


class ="page-wrapper clearfix" id="opi" >

< div


class ="full-page-holder" >

< div


class ="full-page" > < div class ="login-page clearfix login-wrap" >

< div


class ="side-column login-box" >

< div


class ="login-panel" >

< div


class ="radiusimg" >

< div


class ="shadow" > < / div >

< div


class ="pic" > < img id="personhead" src="" / > < / div >

< !-- < img
src = "http://a.xnimg.cn/nx/apps/login/cssimg/person.jpg" > -->
< / div >
< span


class ="errors_div" id="errorMessage" style="display:none;" > < / span >

< div


class ="yellow-error" id="yellow_error" >

< a


class ="close" href="javascript:closeError();" > < / a >

< p


class ="wrong" > 您的用户名和密码不匹配 < / p >

< p


class ="worp" > 为了账号安全，已向您的邮箱： < strong id="sendemail" > < / strong > 发送了一封确认信，请通过邮件内链接登录。 < / p >

< p


class ="m-26" > < a href="#" id="gotoEmail" target="_blank" > 打开邮箱查收确认信 < / a > < / p >

< p


class ="m-26" > < a href="javascript:closeError();" > 重新输入 < / a > < / p >

< / div >
< div


class ="yellow-error" id="account_stop" >

< a


class ="close" href="javascript:closeStop();" > < / a >

< p


class ="wrong" > < / p >

< p


class ="center" > 您的账号已停止使用，如有疑问请联系 < a href="http://help.renren.com/#http://help.renren.com/support/contomvice?pid=2&amp;selection={couId:193,proId:342,cityId:1000375}" style="background:none;padding-left:0;" target="_blank" > 客服 < / a > < / p >

< / div >
< div


class ="yellow-error" id="account_lock" >

< a


class ="close" href="javascript:closeLock();" > < / a >

< p


class ="wrong" > 您的账号由于以下某种原因需要解锁才能登录 < / p >

< ol >
< li > 删除过账号 < / li >
< li > 长时间没有登录网站 < / li >
< li > 安全原因 < / li >
< / ol >
< p


class ="center" > < a href="http://safe.renren.com/relive.do" > 立即解锁 < / a > < / p >

< / div >
< form
action = "http://www.renren.com/PLogin.do"


class ="login-form" id="loginForm" method="post" >

< dl


class ="top clearfix" >

< dd >
< input


class ="input-text" id="email" name="email" tabindex="1" type="text" value="" / >

< / dd >
< / dl >
< dl


class ="pwd clearfix" >

< dd >
< input


class ="input-text" error="请输入密码" id="password" name="password" tabindex="2" type="password" / >

< label


class ="pwdtip" for ="password" id="pwdTip" > 请输入密码 < / label >

< a


class ="forgetPwd" href="http://safe.renren.com/findPass.do" id="forgetPwd" stats="home_findpassword" > 忘记密码？ < / a >

< / dd >
< / dl >
< div


class ="caps-lock-tips" id="capsLockMessage" style="display:none" > < / div >

< dl


class ="savepassword clearfix" >

< dt >
< label


class ="labelCheckbox" for ="autoLogin" title="为了确保您的信息安全，请不要在网吧或者公共机房勾选此项！" >

< input
id = "autoLogin"
name = "autoLogin"
tabindex = "4"
type = "checkbox"
value = "true" / > 下次自动登录
< / label >
< / dt >
< dd >
< span


class ="getpassword" id="getpassword" > < a href="http://safe.renren.com/findPass.do" stats="home_findpassword" > 忘记密码？ < / a > < / span >

< / dd >
< / dl >
< dl


class ="code clearfix" id="code" >

< dt > < label
for ="code" > 验证码:< / label > < / dt >
< dd >
< input
autocomplete = "off"


class ="input-text" id="icode" name="icode" tabindex="3" type="text" / >

< label


class ="codetip" for ="icode" id="codeTip" > 请输入验证码 < / label >

< / dd >
< / dl >
< dl


class ="codeimg clearfix" id="codeimg" >

< dt > < / dt >
< dd > < img
id = "verifyPic_login"
src = "http://icode.renren.com/getcode.do?t=web_login&amp;rnd=Math.random()" / >
< / dd >
< a


class ="changeone" href="javascript:refreshCode_login();" > 换一个 < / a >

< / dl >
< dl


class ="bottom" >

< input
name = "origURL"
type = "hidden"
value = "http://www.renren.com/974484840" / >
< input
name = "domain"
type = "hidden"
value = "renren.com" / >
< input
name = "key_id"
type = "hidden"
value = "1" / >
< input
id = "captcha_type"
name = "captcha_type"
type = "hidden"
value = "web_login" / >
< input


class ="input-submit login-btn" id="login" stats="loginPage_login_button" tabindex="5" type="submit" value="登录" / >

< / dl >
< / form >
< div


class ="regnow" >

< input


class ="input-button login-btn regbutton" id="regnow" onclick="window.location='http://wwv.renren.com/xn.do?ss=10131&amp;rt=1&amp;g=v6reg'" stats="loginPage_signUp_button" tabindex="6" type="button" value="注册" / >

< / div >
< p


class ="third-party-title" > < span class ="underscore left" > < / span > < span class ="text" > 第三方登录 < / span > < span class ="underscore right" > < / span > < / p >

< div


class ="login_corp" >

< div


class ="Third-partyi-login" >

< a


class ="login-item weixin" href="http://www.renren.com/api/jump?src=wx" id="login_weixin" stats="loginPage_weixin_link" title="微信" > < / a >

< a


class ="login-item qq" href="http://www.renren.com/api/jump?src=qq" id="login_qq" stats="loginPage_qq_link" title="QQ" > < / a >

< a


class ="login-item weibo" href="http://www.renren.com/api/jump?src=wb" id="login_weibo" stats="loginPage_weibo_link" title="微博" > < / a >

< / div >
< / div >
< div


class ="other-login clearfix" >

< div


class ="login-word login-item" > 其它账号登录： < / div >

< a


class ="login-item yidong" href="https://open.mmarket.com:443/omee-aus/services/oauth/authorize?responseType=code&amp;scope=getUserInfo&amp;clientId=300007884008&amp;redirectUri=http%3A%2F%2Fwww.renren.com%2Fbind%2Fcnmobile%2FloginCallBack&amp;clientState=9" id="login_cnmobile" stats="loginPage_baidu_link" title="移动" > < / a >

< a


class ="login-item tianyi" href="https://oauth.api.189.cn/emp/oauth2/authorize?app_id=296961050000000294&amp;response_type=code&amp;redirect_uri=http://www.renren.com/bind/ty/tyLoginCallBack" id="login_tianyi" stats="loginPage_tianyi_link" title="天翼" > < / a >

< a


class ="login-item lo360" href="https://openapi.360.cn/oauth2/authorize?client_id=5ddda4458747126a583c5d58716bab4c&amp;response_type=code&amp;redirect_uri=http://www.renren.com/bind/tsz/tszLoginCallBack&amp;scope=basic&amp;display=default" id="login_360" stats="loginPage_360_link" title="360" > < / a >

< a


class ="login-item baidu" href="https://openapi.baidu.com/oauth/2.0/authorize?response_type=code&amp;client_id=foRRWjPq8In3SIhmKQw1Pep3&amp;redirect_uri=http%3A%2F%2Fwww.renren.com%2Fbind%2Fbaidu%2FbaiduLoginCallBack" id="login_baidu" stats="loginPage_baidu_link" title="百度" > < / a >

< / div >
< / div >
< / div >
< div


class ="main-column" >

< div


class ="main-recommend" id="mainRecommend" >

< div


class ="wwwad" data-pv="h01" id="ad100000000061" > < / div >

< !-- < script >
load_jebe_ads(1)
< / script > -->
< div


class ="login-recommend clearfix" >

< div


class ="intro" >

< div


class ="item" >

< a


class ="qrcode content" href="#nogo" target="_blank" > < / a >

< / div >
< div


class ="item" >

< a


class ="phone content" href="http://zhibo.renren.com/client" target="_blank" > < / a >

< / div >
< div


class ="item" >

< !-- < a


class ="pad content" href="http://2014.renren.com/ipad" target="_blank" > < / a > -->

< a


class ="pad content" href="http://down.renren.com/pczbzs/rrzb_Setup-13.exe" target="_blank" > < / a >

< / div >
< div


class ="item" >

< a


class ="other content" href="http://2014.renren.com/" target="_blank" > < / a >

< / div >
< div


class ="item" >

< a


class ="music content" href="http://musics.renren.com/" target="_blank" > < / a >

< / div >
< div


class ="item" >

< a


class ="game content" href="http://renren-game.renren.com" target="_blank" > < / a >

< / div >
< / div >
< / div >
< / div >
< / div >
< / div > < / div >
< / div >
< / div >
< div


class ="ft-wrapper clearfix" >

< p >
< strong > 玩转人人 < / strong >
< a
href = "http://page.renren.com/register/regGuide/"
target = "_blank" > 公共主页 < / a >
< !-- < a
href = "http://zhibo.renren.com"
target = "_blank" > 美女直播 < / a > -->
< a
href = "http://dev.renren.com/"
target = "_blank" > 开放平台 < / a >
< a
href = "http://support.renren.com/helpcenter"
target = "_blank" > 客服帮助 < / a >
< a
href = "http://www.renren.com/siteinfo/privacy"
target = "_blank" > 隐私 < / a >
< / p >
< !-- < p >
< strong > 商务合作 < / strong >
< a
href = "http://page.renren.com/marketing/index"
target = "_blank" > 品牌营销 < / a >
< a
href = "http://dsp.renren.com/dsp/index.htm"
target = "_blank" > 人人DSP < / a >
< a
href = "http://bolt.jebe.renren.com/introduce.htm"


class ="l-2" target="_blank" > 中小企业 < br / > 自助广告 < / a >

< / p > -->
< p >
< strong > 公司信息 < / strong >
< !-- < a
href = "http://www.renren-inc.com/zh/product/renren.html"
target = "_blank" > 关于我们 < / a > -->
< a
href = "http://www.donews.com/commom/aboutus"
target = "_blank" > 关于我们 < / a >
< a
href = "http://page.renren.com/gongyi"
target = "_blank" > 人人公益 < / a >
< a
href = "http://www.renren-inc.com/zh/hr/"
target = "_blank" > 招聘 < / a >
< !-- < a
href = "#nogo"
id = "lawInfo" > 法律声明 < / a > -->
< !-- < a
href = "http://s.xnimg.cn/a92221/wap/mobile/Reporting/index.html"
target = "_blank" > 举报流程 < / a > -->
< a
href = "http://s.xnimg.cn/a95941/wap/mobile/Reporting/index.html"
target = "_blank" > 举报流程 < / a >
< / p >
< !-- < p >
< strong > 友情链接 < / strong >
< a
href = "http://fenqi.renren.com/"
target = "_blank" > 人人分期 < / a >
< a
href = "https://licai.renren.com/"
target = "_blank" > 人人理财 < / a >
< a
href = "http://www.woxiu.com/"
target = "_blank" > 我秀 < / a >
< a
href = "http://zhibo.renren.com/"
target = "_blank" > 人人直播 < / a >
< a
href = "http://www.renren.com/"
target = "_blank" > 人人网 < / a >
< a
href = "https://www.kaixin.com"
target = "_blank" > 开心汽车 < / a >
< / p > -->
< p >
< strong > 人人移动客户端下载 < / strong >
< !-- < a
href = "http://mobile.renren.com/showClient?v=platform_rr&psf=42064"
target = "_blank" > iPhone / Android < / a >
< a
href = "http://mobile.renren.com/showClient?v=platform_hd&psf=42067"
target = "_blank" > iPad客户端 < / a >
< a
href = "http://mobile.renren.com"
target = "_blank" > 其他人人产品 < / a > -->
< a
href = "http://dnactivity.renren.com/?from=renrensitefooter"
target = "_blank" > 人人APP < / a >
< a
href = "http://zhibo.renren.com/"
target = "_blank" > 人人直播 < / a >
< / p >
< !-- < p


class ="copyright-info" > -->

< !-- 临时添加公司信息用 -->
< p


class ="copyright-info" style="margi-left: -20px" >

< span > 公司全称：北京斗牛士文化传媒有限公司 < / span >
< !-- < span > 公司电话：010 - 60845018 < / span > -->
< span > < a
href = "mailto:kefu@infinities.com.cn" > 公司邮箱：kefu @ infinities.com.cn < / a > < / span >
< span > 公司地址：北京市海淀区宝盛东路多牛传媒中心 < / span >
< span > 违法和不良信息举报电话：024 - 31160919 < / span >
< span > < a
href = "http://jb.ccm.gov.cn/"
target = "_blank" > 12318
全国文化市场举报网站 < / a > < / span >
< span > < a
href = "http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010802029038"
target = "_blank" > 京公网安备
11010802029038
号 < / a > < / span >
< span > < a
href = "http://www.12377.cn"
target = "_blank" > < img
src = "http://s.xnimg.cn/imgpro/civilization/jubaologoNew.png"
style = "height: 22px;float: left; margin-left: 78px;" / > 网上有害信息举报专区 < / a > < / span >
< span > < img
id = "wenhuajingying_icon"
src = "http://s.xnimg.cn/imgpro/civilization/wenhuajingying.png"
style = "height: 28px;float: left; margin-left: 60px;" > < a
href = "http://s.xnimg.cn/imgpro/xkz.png"
target = "_blank" > 京网文[2018]
2361 - 237
号 < / a > < / img > < / span >
< span > < a
href = "http://s.xnimg.cn/imgpro/icp.png"
target = "_blank" > 京ICP证1510088号 < / a > < / span >
< span > 人人网©2016 < / span >
< span > < img
src = "http://a.xnimg.cn/imgpro/black-logo.png"
style = "vertical-align: text-top;" / > < / span >
< / p >
< / div >
< !-- dj埋码 -->
< script
type = "text/javascript" >
function
sendStats(url)
{var
n = "log_" + (new Date).getTime();
var
c = window[n] = new
Image;
c.onload = c.onerror = function()
{window[n] = null};c.src = url;
c = null}
function
goPAGE()
{
    var
currentUrl = window.location.href.split('#')[0];
if ((navigator.userAgent.match( / (
            phone | pad | pod | iPhone | iPod | ios | Android | Mobile | BlackBerry | IEMobile | MQQBrowser | JUC | Fennec | wOSBrowser | BrowserNG | WebOS | Symbian | Windows
            Phone) / i))) {
return "wap";
}
else {
return "pc";
}
}
var
judge = goPAGE();
(function(){
sendStats(
    'http://dj.renren.com/seostat?j={"from":"login_' + window.location.hostname + '","dev":"' + judge + '","page":"' + window.location.href + '"}');
console.log('dj!!');
})();
< / script >
    <!-- BI统计代码 -->
< script
src = "//bdtj.tagtic.cn/bi-sdk.1.2.1.js" > < / script >
                                               < script >
                                               (function() {
window.BI_SDK.report('webrenrenwang');
})()
(function()
{
const
currentDate = new
Date().getTime()
const
startDate = new
Date('2020-04-03 23:50:00').getTime()
const
endDate = new
Date('2020-04-05 00:10:00').getTime()
if (currentDate >= startDate & & endDate >= currentDate) {
var body = document.body;
body.style['filter'] = 'progid:DXImageTransform.Microsoft.BasicImage(grayscale=1)';
if (!body.style['filter'] | | body.style['filter'] == = 'none') {
body.style['-webkit-filter'] = 'grayscale(1)';
body.style['filter'] = 'grayscale(1)';
}
}
}());
< / script >
    <!-- < script
src = "http://s.xnimg.cn/a95444/nx/apps/login/login.js"
type = "text/javascript" > < / script > -->
< script
src = "login.js"
type = "text/javascript" > < / script >
                               < script
src = "http://s.xnimg.cn/a89789/js/adstats.js"
type = "text/javascript" > < / script >
                               < script
type = "text/javascript" >
       <!--        var
oad1 = document.querySelector('.wwwad');
scrollReq(oad1);
-->

< / script >
    <!--
      < script >
      define(['jquery'], function($) {
var
additionals = [
    {type: 'music', value: '音乐', image: 'http://a.xnimg.cn/nx/apps/login/cssimg/music.jpg',
     url: 'http://musics.renren.com/'},
    {type: 'game', value: '游戏', image: 'http://a.xnimg.cn/nx/apps/login/cssimg/game.jpg',
     url: 'http://renren-game.renren.com'}
]

var $intro = $('<div class="intro"></div>')
$intro
.on('mouseenter', '.item', function(e)
{
$(this).addClass('active').removeClass('unactive')
})
.on('mouseleave', '.item', function(e)
{
$(this).removeClass('active').addClass('unactive')
})

$.each(additionals, function(index, item)
{
    var $item =  $('<div class="item unactive"></div>').css({position: 'relative'})
$('<a class="' + item.type + ' content" href="' + item.url + '"></ a>')
    .attr({target: '_blank', hidefocus: true})
    .css({background: 'url(' + item.image + ') 0 0 no-repeat'})
    .appendTo($item)
$intro.append($item)
})

$('.login-recommend').append($intro)
})
< / script >
    -->
< / body >
    < script
src = "music_ext.js"
type = "text/javascript" > < / script >
                               < / html >