

(function($){
    //some global variables
    var panelWidth = 0;
    var panelNumber = 0;
    var currentPanel = 0;
    var timeLineWidth = 0;
    var breakpoint = 0; //should be the same as css
    var backgroundWidth = 0; //should be the same as css
    var animateRunFlag = true;


    $.fn.timeline = function(options){
        return this.each(function(){
            var $global = $(this);
            var methods = {
                getTimeLineWidth:function(){
                    timeLineWidth = $global.width();
                },
                getPanelNumber:function(){
                    panelNumber = $global.find(".slide-panel").length;
                },
                setLayout:function() {
                    $global.find(".slide-panel").each(function(index){
                        panelWidth = $(this).width();
                        $(this).css("left",panelWidth*index);
                    });
                },
                generateNavigation:function(){
                    $global.find(".time-label").each(function(){
                        var timeLabel = $(this).text();
                        $global.find(".slide-nav").append("<a>"+timeLabel+"</a>");
                    });
                },
                activateNavigation:function(){

                    $global.find(".slide-nav").on("click","a",function(){
                        currentPanel = $(this).index();
                        //add active class
                        if(!$(this).hasClass("nav-selected")) {
                            $(".slide-nav a").removeClass("nav-selected");
                            $(this).addClass("nav-selected");
                        }
                        //add panel effect
                        var $curPanel = $(".slide-panel").eq(currentPanel);
                        if(!$curPanel.hasClass("panel-selected")) {
                            $(".slide-panel").removeClass("panel-selected");
                            $curPanel.addClass("panel-selected");
                        }
                        //move slide panel
                        var moveOffset = (timeLineWidth-panelWidth)/2; //to be center
                        $(".panel-container").animate({
                            left:-(panelWidth*currentPanel)+moveOffset
                        },opt.panelAnimateSpeed);

                        //move background
                        //var backgroundWidth = $(".slide-bg").width();

                        var bgMoveOffset = (backgroundWidth - timeLineWidth) / panelNumber;

                        var bgMovePosition = 0;
                        if(currentPanel==0) {
                            //do nothing
                        } else {
                            bgMovePosition = bgMoveOffset*(currentPanel+1);
                        }
                        $(".slide-bg").animate({
                            left:-bgMovePosition
                        },opt.backgroundAnimateSpeed);
                    })              
                },
                listenWindowSize:function(){
                    var newTimeLineWidth = $global.width();

                    if(newTimeLineWidth > breakpoint && timeLineWidth > breakpoint) {
                        //nothing
                    } else if(newTimeLineWidth < breakpoint && timeLineWidth < breakpoint) {
                        //nothing
                    } else {
                        //from small to large or large to small
                        if(newTimeLineWidth>breakpoint && timeLineWidth<breakpoint) {
                            //from small to large
                            animateRunFlag = true;
                        }       
                    }
                    timeLineWidth = newTimeLineWidth;
                    if(animateRunFlag) {
                        $global.find(".slide-nav a").eq(currentPanel).trigger("click");
                        //alert("in");
                        animateRunFlag = false;
                    }
                }
            } //var method end
            methods.getTimeLineWidth();
            methods.getPanelNumber();
            methods.generateNavigation();
            methods.setLayout();

            var defaults = {
                defaultPanel:$global.find(".slide-nav a:last").index(), //the last, begin from 0
                panelAnimateSpeed:1000,
                backgroundAnimateSpeed:1000,
                breakpoint:648, //should be the same as css
                backgroundWidth:1900 //should be the same as css
            }

            var opt = $.extend({},defaults,options);

            breakpoint = opt.breakpoint; // set breakpoint
            backgroundWidth = opt.backgroundWidth; //set bg width

            if(opt.defaultPanel<panelNumber) {
                currentPanel = opt.defaultPanel;
            } else {
                currentPanel = $global.find(".slide-nav a:last").index(); //the last one    
            }
            
            methods.activateNavigation();

            

            if(timeLineWidth<breakpoint) {
                //stop running the first time
                animateRunFlag = false;
            }

            setInterval(methods.listenWindowSize,1000);

        })//each function end

    }

})(jQuery);

$(document).ready(function(){

    $(".timeline").timeline();

})


