var status = 1;
var Menus = new DvMenuCls;

document.onclick=Menus.Clear;
function showmenu(id){id.style.visibility = "visible";}
function hidmenu(){UserList.style.visibility = "hidden";}
function switchSysBar(){
	var switchPoint=document.getElementById("switchPoint");
	var frmTitle=document.getElementById("frmTitle");
	var table=document.getElementById("showinfo");
	if ( null == table) {
		table=document.getElementById("showUserinfo");
	}
    	if (1 == window.status){
        	window.status = 0;
	        frmTitle.style.display="none"
	        if ( null != table) {
        	    table.style.width="95%"
		}
	}
	else{
		window.status = 1;
		frmTitle.style.display=""
		if ( null != table) {
			table.style.width="80%"
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



// Modify user

function subModUser(userId , userName){
    var password = $("#password").val()
    var admin = $("select[name='admin']").val()
    // ajax
    if ('6' > password.length){
        $("#CheckReP").text('* Num of pass less then 6')
    }
    else{
        urltmp = "/usermanage/ModUser/?userid=" + userId + "&password=" + password
        + "&admin=" + admin + "&username=" + userName
        $.getJSON(urltmp, function(ret){
            if ('success' == ret['result']){
                window.location.href="#close"
                $("#buttonUser").click()
            }
            else{
                $("#CheckReU").text('* Modify user info fail.')
                $("#CheckReP").text('* Maybe DB is dead.')
            }
        })
    }
}
function ModUserInfo(userId, userName){
    $.ajax({
            type: "POST",
            url: "/usermanage/ShowUserHTMLTemplate/",
            data: {'do': 'mod', 'userId': userId, 'userName': userName},
            success: function(data){
                $("#openModal").html( data )
            }
        }
    );
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
    window.location.href="#close"
    urltmp = "/usermanage/DelUser/?userid=" + userId
    $.ajax({url:urltmp,async:false});
    $("#buttonUser").click()
}


//---add user---

// submit add user form
function subAddUser(){
    // check user whether exist
    var username = $("#username").val()
    var password = $("#password").val()
    if ('0' == username.length){
        $("#CheckReU").text('* Empty!')
        if ('6' > password.length){
            $("#CheckReP").text('* Num of pass less then 6')
        }
        else{
            $("#CheckReP").empty();
        }
    }
    else{
        $("#CheckReU").empty();
        urltmp = "/usermanage/CheckUser/?username=" + username
        $.getJSON(urltmp, function(ret){
            if ('success' == ret['result']){
                if ('6' > password.length){
                    $("#CheckReP").text('* Num of pass less then 6')
                }
                else{
                    $("#CheckReP").empty();
                    $("#CheckReU").empty();
                    $('#adduserform').submit()
                }
            }
            else{
                $("#CheckReU").text('already exit!')
            }
        })
    }
}
function CleanAddUser() {
	$('#adduserform')[0].reset();
	$("#CheckReP").empty();
	$("#CheckReU").empty();
}
function AddUser(){
    $.ajax({
        type: "POST",
        url: "/usermanage/ShowUserHTMLTemplate/",
        data: {'do': 'add'},
        success: function(data){
            $("#openModal").html( data )
        }
    });
    window.location.href="#openModal"
}


//---add user end---
