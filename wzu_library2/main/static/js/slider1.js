var autoplay = true;
var autoplay_Delay = 6000; // ms
var autoplayId;
var intervalId;

var slider;
var slider_item_container;
var slider_items;
var indicator_container;

var slider_item_width;
var curIndex = 0;

window.onload = function() {
    initElement();
    initEvent();
    if (autoplay) {
        startAnimation(slider_item_container);
    }
}

function initElement() {
    slider = document.getElementById("slider");
    slider_items = slider.getElementsByClassName("slider-items");//bttag li
    slider_item_container = slider.getElementsByClassName("slider-item-container")[0];
    indicator_container = slider.getElementsByClassName("indicator-container")[0];
    
    var firstItem = slider_items[0].cloneNode(true);//复制第一张图片
    slider_item_container.appendChild(firstItem);//把slider-items(li)的内容增加到slider-item-container(ul)内
    slider_item_width = slider_items[0].offsetWidth;//统一长度
    // console.log(slider_item_container)
}

function initEvent() {
    slider.addEventListener("mouseover", function () {
        clearTimeout(autoplayId);
        autoplay = false;
    });
    slider.addEventListener("mouseout", function () {
        autoplay = true;
        startAnimation(slider_item_container);
    });
    
    var indicators = indicator_container.children;//小圆点
    for (var i = 0; i < indicators.length; i++) {//遍历圆点
        indicators[i].setAttribute("index", i);//设置索引值
        indicators[i].addEventListener("click", function () {
            var index = parseInt(this.getAttribute("index"),10);//索引值统一为十进制（第二参数我补的）
            next(index);
        });
    }
    
    var left_arrow = slider.getElementsByClassName("left-arrow")[0];
    var right_arrow = slider.getElementsByClassName("right-arrow")[0];
    left_arrow.addEventListener("click", function () {
        prev();
    });
    right_arrow.addEventListener("click", function () {
        next();
    });
}

function animate(element, target) {
    var step = 500;
    var time = 40;
    //element.offsetLeft element的左边界与节点左边界的距离
    var gap = (Math.abs(target - element.offsetLeft) / slider_item_width);
    // console.log("gap=",gap)//左右按键=1
    if (gap > 1) {
        step = step * gap;
        time = time / gap;
    }
    if (element) {
        step = (element.offsetLeft > target) ? -step : step;//if a>b s=-s else s=s
        clearInterval(intervalId);//类似cleartimeout，清除setinterval(L77)设定的值
        setCurrentActiveIndicator(curIndex);//小圆点的状态变化
        intervalId = setInterval(function () {//每隔time时间调用function函数
            if ((step < 0) && (Math.abs(element.offsetLeft + step) < Math.abs(target))) {
                element.style.left = element.offsetLeft + step + "px";
            } else {
                if (Math.abs(target - element.offsetLeft) > Math.abs(step)) {
                    element.style.left = element.offsetLeft + step + "px";
                } else {
                    clearInterval(intervalId)
                    intervalId = -1;
                    element.style.left = target + "px";
                    if (autoplay) {
                        startAnimation(element);
                    }
                }
            }
        }, time);
    }
}

function prev() {//切换上一张
    var element = slider_item_container;
    var li = element.children;
    curIndex = curIndex - 1;
    if (curIndex < 0) {
        element.style.left = -((li.length-2)*slider_item_width) + "px";//
        curIndex = li.length-3;//
    }
    // console.log("liLen",li.length)
    // console.log("curIndex",curIndex)
    // console.log(-(curIndex*slider_item_width));
    animate(element, -(curIndex*slider_item_width));//target为-当前应该显示的图片的相对于拼接图片的距离
}

function next(nextIndex) {//切换下一张
    var element = slider_item_container;
    var li = element.children;
    if ((nextIndex != null) && (typeof(nextIndex) != "undefined")) {
        curIndex = nextIndex;
    } else {
        curIndex = curIndex + 1;
        if (curIndex > (li.length-2)) {//
            element.style.left = 0 + "px";
            // curIndex = 1;
            curIndex = 0;
        }
    }
    // console.log("liLen",li.length)
    // console.log("curIndex",curIndex)
    // console.log(-(curIndex*slider_item_width));
    animate(element, -(curIndex*slider_item_width));
}

function startAnimation(element) {
    if (autoplayId) {
        clearTimeout(autoplayId);//重置计时器，猜测是停止自动切换图片
    }
    autoplayId = setTimeout(function () {
        next();//autoplay_Delay到时间后执行function函数
    }, autoplay_Delay);
}

function setCurrentActiveIndicator(index) {//图片下方小圆点的控制！！！！！！有误！
    var indicators = indicator_container.children;
    if (index == indicators.length) {
        index = 0;
    }
    for (var i = 0; i < indicators.length; i++) {
        if (i == index) {
            indicators[i].className = "indicator active";
        } else {
            indicators[i].className = "indicator";
        }
    }
}
