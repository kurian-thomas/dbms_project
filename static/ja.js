var x = document.getElementById("sign_in").elements;

 function get_element_signup(){
 	console.log("in get");
 	var n=x[0].value;
 	var p=x[1].value;
 	var ad=x[2].value;
 	var em=x[3].value;
 	$('.ajaxProgress').show();
 	$.ajax({
 		type:"POST",
 		url:"http://127.0.0.1:8000/tc/get_element/",
 		datatype:"json",
 		async:true,
 		data:{
 			csrfmiddlewaretoken:'{{ csrf_token }}',
 			name:n,
 			admission:ad,
 			email:em,
 			pass:p,
 		},
 		success: function(json){
 			console.log("sucess");
 			var sb=document.getElementById("sigbutton");
 			sb.setAttribute('href',"http://127.0.0.1:8000/tc/login/");
 			window.location.href=sb.getAttribute("href");
 			$('.ajaxProgress').hide();
 		}
 	});
 } 

function get_element_log(){
 	console.log("in login");
 	var n=$("#ad").val();
 	var p=$("#pass").val();

 	$('.ajaxProgress').show();
 	$.ajax({
 		type:"POST",
 		url:"http://127.0.0.1:8000/tc/get_element_log/",
 		datatype:"json",
 		async:true,
 		data:{
 			csrfmiddlewaretoken:'{{ csrf_token }}',
 			ad:n,
 			pass:p,
 		},
 		success: function(data){
 			var lb=document.getElementById("logbutton");
 			var welcome=document.getElementById("username");
 			console.log("sucess");
 			console.log(data.l);
 			if(data.l){
 					lb.setAttribute('href',"http://127.0.0.1:8000/tc/dashboard/");
 					//welcome.innerHTML="Welcome "+n;
 					window.location.href=lb.getAttribute("href");
 					
 			}
 			else{
 				alert("password or username is incorrect");
 			}
 			$('.ajaxProgress').hide();
 		}
 	});
 			
 } 

function get_element_adminlog(){
 	console.log("in ad_login");
 	var n=$("#admin_name").val();
 	var p=$("#admin_pass").val();
 	//console.log(n+" "+p);
 	$('.ajaxProgress').show();
 	$.ajax({
 		type:"POST",
 		url:"http://127.0.0.1:8000/tcadmin/get_element_adminlog/",
 		datatype:"json",
 		async:true,
 		data:{
 			csrfmiddlewaretoken:'{{ csrf_token }}',
 			name:n,
 			pass:p,
 		},
 		success: function(data){
 			//var lb=document.getElementById("logbutton");
 			console.log("sucess");
 			// console.log(data.l);

 			// if(data.l){
 			// 		lb.setAttribute('href',"http://127.0.0.1:8000/tc/dashboard/");
 			// 		window.location.href=lb.getAttribute("href");
 			// }
 			// else{
 			// 	alert("password or username is incorrect");
 			// }
 			$('.ajaxProgress').hide();
 		}
 	});
 			
 } 

 


