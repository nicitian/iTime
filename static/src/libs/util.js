

let util = {
    ajaxCallBack(res,info,self,back=false,toUrl=''){
        console.log(res,info,back,toUrl)
        
        if(res.data.success)
        {        
            self.success(info);     
            if(back)                                
                setTimeout(function toLogin(){window.location.href =toUrl;},1200);
            return true
        }
         else
         {                         
            self.error(res.data.err);
            return false
         }   
    }

};
util.title = function (title) {
    title = title ? title + ' - Home' : 'iView project';
    window.document.title = title;
};

export default util;