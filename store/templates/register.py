'''
 
                     




{% extends 'base.html' %}
{% block content %}

<!-- Header-->
        <header class="bg-dark py-5">
            <div class="container px-4 px-lg-5 my-5">
                <div class="text-center text-white">
                    <h1 class="display-4 fw-bolder">Registrate...</h1>
                    <p class="lead fw-normal text-white-50 mb-0">Registrate completando el formulario...</p>
                </div>
            </div>
        </header>

        <div class="container">
        	<div class="row">
        		<center>
        			<div class="col-8">
        				<br/><br/>
                <!-- acá mando el formulario de logeo en tipo post -->
                <form method="POST" action="{% url 'register' %}">
                  {% csrf_token %}
                  
                  {{ form.as_p }}
                  <br/><br/>
                  <button type="submit" class="btn btn-secondary">
                    Register
                  </button>
                
              </form>
              
<br/><br/> 
<br/><br/>
<br/><br/>
        			</div>
        		</center>
        	</div>
        </div>

{% endblock %}


'''

