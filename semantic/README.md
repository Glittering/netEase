#!README


#2017年 03月 17日 星期五 00:10:53 CST
##semantic UI 
1. 基础样式
    + div class = 'ui segment'
    + ui segments
    + ui container segment
    + h1 class='ui header'
    + button class='ui button'
    + div class='ui image'
        img ..
    + 
2. 使用‘形容词’改变样式
    + inverted+color  
    + vertical
    + horizontal
    + (very) padded
    + raised
    + stacked
    + tall stacked
    + piled
    + color
    + secondary
#Segment
##states
    + disabled
    + loading
##variations
    + interted
    + attached
        ui top attached header  --> h5
	ui attached segment
	ui attached header
	ui bottom attached <warning> message
    + padded
    + compact
    + colored
        - red
	- orange 
	- yellow
	- olive
	- green
	- Teal
	- blue
	- violet
	- purple
	- pink
	- brown
	- grey
	- black
    + emphasis
        - secondary
	- tertiary
    + circular
        - ui header
	    sub header
    + clearing
    + floated
    + text Alignment
        - right left center aligned
    + basic
#Header
##Types
    + Page Headers
    + Content
        - huge
        - large
        - medium
        - small
        - tiny
    + icon
        h2 class ui icon header
	    i class settings icon
	    div class content
	        div class sub header
    + sub
        ui sub header
##Content
    + image
        h2 ui header
	    img class ui image src...
	    div class content
        ui circular image
    + icon i中
        - plug icon
	- setting icon
    + subheader
        h2 class ui header
	    div class sub header
##States
    + disabled
##Variations
    + ui dividing header
    + ui block header
    + attached
        h3 class="ui top attached header"
	div class="ui attached segment"
	h3 class="ui attached header"
	div class="ui attached segment"
	h3 class="ui bottom attached header"
    + floating   clearing  right/left floated
    + ui justified header
#image
1. ui small image     can use on img or father obj of image
## variations
1. avatar
2. bordered
3. fluid
4. rounded
5. circular
6. top aligned
   middle aligned
   bottom aligned
7. centered
8. spaced
9. left floated
10. Groups
    <div class="ui tiny images">
      <img class="ui image" src="/images/wireframe/image.png">
      <img class="ui image" src="/images/wireframe/image.png">
    </div>
##button
1. primary
2. secondary
3. visible content
   hidden content
4. fade 渐变
<div class="ui left labeled button" tabindex="0">
  <a class="ui basic right pointing label">
    2,048
  </a>
  <div class="ui button">
    <i class="heart icon"></i> Like
  </div>
</div>
5. ui icon button
6. ui labeled icon button


#2017年 03月 27日 星期一 08:45:04 CST
## landing page
1. loading..


#2017年 03月 28日 星期二 20:24:01 CST
1. 用text使控件透明
2. patted减小占位
3. bodderless 取消边界和menu组件中边界
4. secondary 来做一个高达上的灰色背景色
5. basic 消除组件边界
6. fluid num item 在menu中可以均匀布满一行。
##CSS
1. box-sizing: border-box;

#2017年 03月 29日 星期三 21:05:44 CST
##定位
1. absolute 不会占位 绝对 父级一定要有position  否则会上级一直找到body
2. relative 依旧占位 相对 
3. 万能居中    
    + position:absolute;
    + left:50%;
    + top:50%;
    + transform: translate(-50%, -50%);


#2017年 04月 10日 星期一 18:00:37 CST
##what the fuck?
1. 页面异常捕获
2. 根据页面显示内容的不同来判断按钮状态
3. 实现 分页 
4. 异常
##maybe it's right
1. 分页原理
fake制作假数据
2. 






##others
*loram* 打乱顺序的拉丁文
*i*: class= 'warning icon'

