/* Project specific Javascript goes here. */
$(document).ready(function(){

  $('.input').focus(function(){
    $(this).parent().find(".label-txt").addClass('label-active');
  });

  $(".input").focusout(function(){
    if ($(this).val() == '') {
      $(this).parent().find(".label-txt").removeClass('label-active');
    };
  });

  var signup = $("#signup-form");
  var error = $("#error");
  error.hide();

  var signin = $("#signin-form");


  signup.submit(function (event) {
      event.preventDefault();
      var submitBtn = $(this).find('button[type=submit]');
      submitBtn.prop('disabled', true);
      var data = $(this).serialize();

      $.ajax({
          url: "/api/user/",
          type: "POST",
          data: data,

          success: function (resp) {
              error.hide();
              submitBtn.prop('disabled', true);
              window.location.replace("/signin/");
          },

          statusCode: {
        400: function(resp) {
            error.show();
            $("#error-label").append('Email: ' + resp['responseJSON']['email'][0])
            submitBtn.prop('disabled', false);
        }
      }


      });
  });



  signin.submit(function (event) {
      event.preventDefault();
      var submitBtn = $(this).find('button[type=submit]');
      submitBtn.prop('disabled', true);
      var data = $(this).serialize();

      $.ajax({
          url:"/api/token/",
          type: "POST",
          data: data,

          success: function (resp,) {
              error.hide();
              submitBtn.prop('disabled', true);

                window.localStorage.setItem("Authorization", "Bearer " + resp['access']);
                window.localStorage.setItem("refresh", resp['refresh']);
              window.location.replace("/home/");


          },

          statusCode: {
        400: function(resp) {
            $("#error-signin").empty();
            error.show();
            $("#error-signin").append('Email: ', resp['responseJSON']['non_field_errors'][0]);
            submitBtn.prop('disabled', false);
        }
      }


      });
  });


  /////////////////////////////////////////////////////////////////////////////////////////////
    ////////////////// TimeLine //////////////////////////////////////////////////////////////

  var timeline = $("#timeline");

  function rendering_data(data) {
                for(key in data['results']){

                timeline.append('<div class="col-lg-6">\n' +
                          '    <blockquote class="quote-box">\n' +
                          '      <p class="quotation-mark">\n' +
                          '        “\n' +
                          '      </p>\n' +
                          '      <p class="quote-text">\n' +
                          data['results'][key]['content'] +
                          '      </p>\n' +
                          '      <hr>\n' +
                          '      <div class="blog-post-actions">\n' +
                          '        <p class="blog-post-bottom pull-left">\n' +
                          data['results'][key]['user']['first_name'] + '  '+ data['results'][key]['user']['last_name']+
                          '        </p>\n' +
                          '        <p class="blog-post-bottom pull-right">\n' +
                          '          <span class="badge quote-badge">'+ new Date(data['results'][key]['created'])+ '</span>  \n' +
                          '        </p>\n' +
                          '      </div>\n' +
                          '    </blockquote>\n' +
                          '</div>')

                }
  }




  $.ajax({
      url: "/api/posts/",
      type: "GET",
      success: function (resp) {
                rendering_data(resp)

          //// I didnt have time to handle pagination in html and ajax but response has previous and next
          /// to call server and fetch data



      }
  });


  ////////////////////////////////////////////////////////////////////////////////////////////////
    ///////////////////////// Add New Post ///////////////////////////////////////////////////////
  var post_form = $("#post-form");

  post_form.submit(function (event) {
      event.preventDefault();

      var submitBtn = $(this).find('button[type=submit]');
      submitBtn.prop('disabled', true);
      var data = $(this).serialize();

      var token = window.localStorage.getItem("Authorization");
      var refresh = window.localStorage.getItem("refresh");

              $.ajax({
          url: "/api/posts/",
          type: "POST",
          data: data,
          headers: {"Authorization": token},

          success: function (resp) {
              window.location.replace("/home/");

              // $.ajax({
              //     url: "/api/token/refresh/",
              //     type: "POST",
              //     data: {'refresh': refresh},
              //
              //     success: function (resp) {
              //         window.localStorage.setItem("Authorization", "Bearer " + resp['access']);
              //         window.localStorage.setItem("refresh", resp['refresh']);
              //
              //
              //     }
              // });

          }




      });


  });




});
