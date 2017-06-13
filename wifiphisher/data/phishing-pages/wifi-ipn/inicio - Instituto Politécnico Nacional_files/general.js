/**************************************/
$(document).ready(function(){
		var min=13;
		var max=18;
		function increaseFontSize() {
		   var p = document.getElementsByTagName('p');
		   for(i=0;i<p.length;i++) {
			  if(p[i].style.fontSize) {
				 var s = parseInt(p[i].style.fontSize.replace("px",""));
			  } else {
				 var s = 13;
			  }
			  if(s!=max) {
				 s += 1;
			  }
			  p[i].style.fontSize = s+"px"		
		   }
		}
		function decreaseFontSize() {
		   var p = document.getElementsByTagName('p');
		   for(i=0;i<p.length;i++) {
			  if(p[i].style.fontSize) {
				 var s = parseInt(p[i].style.fontSize.replace("px",""));
			  } else {	
				 var s = 13;
			  }
			  if(s!=min) {		
				 s -= 1;
			  }
			  p[i].style.fontSize = s+"px"
		   }
		}
/***********************************************************/
		function  link1(){window.open('http://www.ipn.mx/Documents/Directorio.pdf');}
		function  twt(){window.open('https://twitter.com/IPN_MX');}
		function  face(){window.open('https://www.facebook.com/pages/Instituto-Polit%C3%A9cnico-Nacional-Oficial/257328147627744');}
		function  google(){window.open('https://plus.google.com/b/103841476689221632363/103841476689221632363');}
		function  yutu(){window.open('http://www.youtube.com/user/IPNoficial');}
		function  rss(){window.open('http://www.ipn.mx/Paginas/rss.aspx');}
		function  cgsi(){window.open('http://www.cgsi.ipn.mx');}
		function  blog(){window.open('http://ipn-mx.blogspot.mx');}
		function openDialog() {
		            $('#overlay').fadeIn('fast', function() {
		                $('#popup').css('display','block');
		                $('#popup').animate({'left':'30%'},500);
		            });
		        }
		        function closeDialog(id) {
		            $('#'+id).css('position','absolute');
		            $('#'+id).animate({'left':'-100%'}, 500, function() {
		                $('#'+id).css('position','fixed');
		                $('#'+id).css('left','100%');
		                $('#overlay').fadeOut('fast');
		            });
		        }       
		        /**Alerta salida del sitio**/ 
		        function salidaIPN() {
		 		   alert("En este momento abandona el sitio oficial del IPN");
				}
		        /***Alerta salida del sitio*****/


});
/**************************************/
$(document).ready(function(){
	$("#carousel .es-carousel").after("<div class='es-nav'><span class='es-nav-prev'>Previous</span><span class='es-nav-next'>Next</span></div>");
	$(".es-nav-next").hover(function(){
	$("#carousel .es-carousel ul").animate({marginLeft:-1000},500);
	$(this).first("li").after
	});
/**/
var menuva = ".menu-vertical ul li span.static";
var menuv = "#s4-leftpanel";
var menuh = ".toggleMenu";/*".menu-horizontal";*/
var menuhc = "#ctl00_TopNavigationMenuV4";
var activo = ".menu-vertical ul li ul li.selected";

$(menuv).before("<div class='triggerv'>Men&uacute; Secundario</div>");
$(menuh).before("<div class='triggerh'><div class='escudo'></div><span><a href='/'>Instituto Politécnico Nacional<span>'La Técnica al Servicio de la Patria'</span></a></span></div>");

/*Si está activo*/
	$(activo).closest("ul").css({"display":"block"});
	$(activo).parents("li").find("span.static").addClass("on");	
	/*Si presionan el botón*/
	$(menuva).click(function(){
	$(this).parent().find("ul").stop().slideToggle();
	$(this).toggleClass("on");		
	});
	$(".triggerh").click(function(){
	$(".menu-horizontal").stop().slideToggle();
	});

/*	$(".triggerv").click(function(){
	$(menuv).stop().toggle("slide");
	});*/
	$(".triggerv").click(function(){
	$(menuv).stop().slideToggle();
	});

});

function ocultarMostrar(id){
		clave = document.getElementById(id);
		if(clave.style.display=='block'){
			clave.style.display='none';
		}
		else{
			clave.style.display='block';
			
			}
	}




