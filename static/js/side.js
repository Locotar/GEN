var status = 1;
var Menus = new DvMenuCls;

document.onclick=Menus.Clear;
function showmenu(id){id.style.visibility = "visible";}
function hidmenu(){UserList.style.visibility = "hidden";}
function switchSysBar(){
    var switchPoint=document.getElementById("switchPoint");
	var frmTitle=document.getElementById("frmTitle");
	var table=document.getElementById("showinfo");
    if (1 == window.status){
        window.status = 0;
        //alert(table);

        //switchPoint.style.backgroundImage = 'url(images/common/left.gif)';
        frmTitle.style.display="none"
        if ( null != table) {
            table.style.width="98%"
        }
    }
    else{
        window.status = 1;
        //switchPoint.style.backgroundImage = 'url(images/common/right.gif)';
        frmTitle.style.display=""
        if ( null != table) {
            table.style.width="84%"
        }
    }
}

function DvMenuCls(){
	var MenuHides = new Array();
	this.Show = function(obj,depth){
		var childNode = this.GetChildNode(obj);
		if (!childNode){return ;}
		if (typeof(MenuHides[depth])=="object"){
			this.closediv(MenuHides[depth]);
			MenuHides[depth] = '';
		};
		if (depth>0){
			if (childNode.parentNode.offsetWidth>0){
				childNode.style.left= childNode.parentNode.offsetWidth+'px';
				
			}else{
				childNode.style.left='100px';
			};
			
			childNode.style.top = '-2px';
		};

		childNode.style.display ='none';
		MenuHides[depth]=childNode;
	
	};
	this.closediv = function(obj){
		if (typeof(obj)=="object"){
			if (obj.style.display!='none'){
			obj.style.display='none';
			}
		}
	}
	this.Hide = function(depth){
		var i=0;
		if (depth>0){
			i = depth
		};
		while(MenuHides[i]!=null && MenuHides[i]!=''){
			this.closediv(MenuHides[i]);
			MenuHides[i]='';
			i++;
		};
	
	};
	this.Clear = function(){
		for(var i=0;i<MenuHides.length;i++){
			if (MenuHides[i]!=null && MenuHides[i]!=''){
				MenuHides[i].style.display='none';
				MenuHides[i]='';
			}
		}
	}
	this.GetChildNode = function(submenu){
		for(var i=0;i<submenu.childNodes.length;i++)
		{
			if(submenu.childNodes[i].nodeName.toLowerCase()=="div")
			{
				var obj=submenu.childNodes[i];
				break;
			}
		}
		return obj;
	}

}


function getleftbar(obj){
	var leftobj;
	var titleobj=obj.getElementsByTagName("a");
	leftobj = document.all ? frames["frmleft"] : document.getElementById("frmleft").contentWindow;
	if (!leftobj){return;}
	var menubar = leftobj.document.getElementById("menubar")
	if (menubar){
			if (titleobj[0]){
				document.getElementById("leftmenu_title").innerHTML = titleobj[0].innerHTML;
			}
			var a=obj.getElementsByTagName("ul");
			for(var i=0;i<a.length;i++){
				menubar.innerHTML = a[i].innerHTML;
				//alert(a[i].innerHTML);
			}
	}
}







// ----------------- body ----------------

// ++++ ENV
// do something at load
$(function(){
    var mydate = new Date();
    var timeNow=mydate.toLocaleString();
    $("#showCurrentTime").html(timeNow)

    // -----------------login
    if(document.getElementById("loginForm")){
    alert('Regist Success.')
}
});

// show jump div
function showenvInfo(envId){
    // get value from sql;
    var text="<div><a href=\"#close\" title=\"Close\" class=\"close\">X</a><h2>节点信息</h2>"
    text = text + "<p>" + envId + "</p></div>"
    $("#openModal").html( text )
    window.location.href="#openModal"
}

function deleteEnv(envId ){
    // get value from sql;
    var text="<div><a href=\"#close\" title=\"Close\" class=\"close\">X</a><h2>确定删除</h2>"
    text = text + "<p> 确定要删除么？</p></div>"
    $("#openModal").html( text )
    window.location.href="#openModal"
}

function RstartEnv(envId ){
    // get value from sql;
    var text="<div><a href=\"#close\" title=\"Close\" class=\"close\">X</a><h2>确定重启</h2>"
    text = text + "<p> 确定要重启么？</p></div>"
    $("#openModal").html( text )
    window.location.href="#openModal"
}

// click the flash Env button
$("#buttonEnv").click(function() {
    var mydate = new Date();
    var timeNow=mydate.toLocaleString();
    $("#showCurrentTime").html(timeNow)
    // ajax
    var htmlobj=$.ajax({url:"/getEnvFromDB/",async:false});
    $("#showinfo").html(htmlobj.responseText);
});




// ++++ User
// click the flash buttonUser button
$("#buttonUser").click(function() {
    var mydate = new Date();
    var timeNow=mydate.toLocaleString();
    $("#showCurrentTime").html(timeNow)
    // ajax
    var htmlobj=$.ajax({url:"/usermanage/ShowUser/",async:false});
    $("#showUserinfo").html(htmlobj.responseText);
});

// show jump div
function ModUserInfo(userId){
    // get value from sql;
    var text="<div><a href=\"#close\" title=\"Close\" class=\"close\">X</a><h2>用户信息</h2>"
    text = text + "<p>" + userId + "</p></div>"
    $("#openModal").html( text )
    window.location.href="#openModal"
}

function deleteUser(userId ){
    // get value from sql;
    var text="<div><a href=\"#close\" title=\"Close\" class=\"close\">X</a><h2>确定删除</h2>"
    text = text + "<br/><p> 确定要删除么？</p><br/><br/>"
    text = text + "<button onclick=\"deleteUserSure(" + userId + ")\"> ok</button></div>"
    $("#openModal").html( text )
    window.location.href="#openModal"
}

function deleteUserSure(userId){
//    alert(userId)
    window.location.href="#close"
    urltmp = "/usermanage/DelUser/?userid=" + userId
    $.ajax({url:urltmp,async:false});
    $("#buttonUser").click()
    $("#buttonUser").click()
}

function AddUser(){
    var text="<div><a href=\"#close\" title=\"Close\" class=\"close\">X</a><h2>添加用户</h2>"
    text = text + "<form method = 'post' enctype=\"multipart/form-data\" action='/usermanage/AddUser/'>"
    text = text + "<br/><div>&nbsp&nbsp&nbsp<label>用户名:</label>&nbsp<input name=\"username\" type=\"text\"/></div>"
    text = text + "<br/><div>&nbsp&nbsp&nbsp<label>密码:&nbsp</label>&nbsp&nbsp&nbsp&nbsp<input name=\"password\" type=\"password\"/></div>"
    text = text + "<br/><div>&nbsp&nbsp&nbsp<label>管理员:&nbsp</label><select name='admin' type=\"text\"><option value=\"N\">N</option>"
    text = text + "<option value=\"Y\">Y</option></select></div>"
    text = text + "<br/><br/><div><hr/></div>"
    text = text + "<div><button type=\"submit\" >提交</button>&nbsp&nbsp&nbsp<button id=\"reset\" type=\"button\">重置</button></div>"
//    text = text + ""onClick=\"sub()\"
    text = text + "</form>"
    text = text + "</div>"
    $("#openModal").html( text )
    window.location.href="#openModal"
}

