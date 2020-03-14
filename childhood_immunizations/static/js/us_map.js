var divElement = document.getElementById('viz1584142540183');                    
var vizElement = divElement.getElementsByTagName('object')[0];                    
vizElement.style.width='1250px';vizElement.style.height='795px';                    
var scriptElement = document.createElement('script');                    
scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
vizElement.parentNode.insertBefore(scriptElement, vizElement);      