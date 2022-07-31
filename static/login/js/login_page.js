function send_otp() {

    var email=document.getElementById ("email").value
    var password=document.getElementById ("password").value
    

  
      $.ajax({
        url: "/auth/send-otp",
        data: {
          email: email,
          password: password,
        },
        
        success: function (data) {

          console.log(data);
          if(data["isUserAuthorized"]=="True"){
            alert("otp send succesfully")
          }
          else{
            alert("email or password is invalid")
          }
        }
          
    });
  }