define(['jquery',"bootstrap","underscore"],function ($,bootstrap,_) {
    var helper = {
        requestPool:[],
        api:function(opts,curTry){
            var self = this;
            curTry = curTry || 0;
            if(!opts.url || _.contains(self.requestPool,opts.url)){
                return;
            }
            NProgress && NProgress.start();
            self.requestPool.push(opts.url);
            opts = $.extend({
                    type:"get",
                    url:"",
                    data:{},
                    dataType:"json"},opts || {});
            return $.ajax(opts).done(function(data){
                self.requestPool =_.filter(self.requestPool,function(item){
                    item !== opts.url;
                });
                if(opts.done){
                    NProgress && NProgress.done();
                    return opts.done.apply(this,[data]);
                }
            }).fail(function(data){
                self.requestPool =_.filter(self.requestPool,function(item){
                    item !== opts.url;
                });
                curTry ++;
                if(curTry < 5){
                    return self.api(opts,curTry);
                }
                NProgress && NProgress.done();
                if(opts.fail){
                    return opts.faild.apply(this,[data]);
                }
            }).always(function(data){
                self.requestPool =_.filter(self.requestPool,function(item){
                    item !== opts.url;
                });
            });
        },
        test:function(a){

        }
    }
    return helper;
});
