'use strict';
var animateApp = angular.module('animateApp', ['ui.router', 'ngAnimate','ng-backstretch','ngMaterial','ngSanitize']);
animateApp.config(function ($stateProvider,$urlRouterProvider,$sceProvider) {

    $urlRouterProvider.otherwise('/home');
    $stateProvider
        .state('home',{
            url: '/home',
            templateUrl:'static/partials/home.html',
            controller:'mainController'
        })
        .state('contact',{
            url: '/contact',
            templateUrl:'static/partials/contact.html',
            controller:'contactController'
        })
        .state('about',{
            url: '/about',
            templateUrl:'static/partials/about.html',
            controller:'aboutController'
        })
        .state('classes',{
            url: '/classes',
            templateUrl:'static/partials/classes.html',
            controller:'classesController'
        })
});


// CONTROLLERS ============================================
// home page controller
animateApp.controller('mainController', function($rootScope,$scope,$http,$state,$mdDialog) {
    $scope.images = [
    '/static/img/login/1.jpg',
    '/static/img/login/2.jpg'
  ];
    $rootScope.user={
        'NetID':'taobupt',
        'password':''
    };
    $scope.submitForm = function() {
        if ($scope.loginForm.$valid) {
            $http({
                url:'http://127.0.0.1:5000/login',
                method:'post',
                params:{'NetID':$rootScope.user.NetID,'password':$rootScope.user.password}
            }).then(function (response) {
                var error = response.data;
                if (error===null){
                    $state.go('classes');
                }else{
                    $state.go('home');
                    $mdDialog.show(
                      $mdDialog.alert()
                        .parent(angular.element(document.querySelector('#popupContainer')))
                        .clickOutsideToClose(true)
                        .title('NetID or Password is Wrong')
                        .textContent('The credentials you provided cannot be determined to be authentic!')
                        .ariaLabel('Alert Dialog Demo')
                        .ok('Try Again')
                    );
                }
            },function (error) {
                window.alert(error);
            })
        }
    }
});

// about page controller
animateApp.controller('aboutController', function($scope) {
    $scope.pageClass = 'page-about';
});

// contact page controller
animateApp.controller('contactController', function($scope) {
    $scope.pageClass = 'page-contact';
});

animateApp.controller('classesController', function($scope,$rootScope,$sce) {
    var text = "<input type='button' value='Select' class='btn btn-warning btn-xs'>";
    text = $sce.trustAsHtml(text);
    $rootScope.classes=[
        {'Select':text,'CRN':'33086','Subj':'CSCE','Crse':'233','Sec':'600','Cmp':'CS','Cred':'3','Title':'MACHINE LEARNING\n\n\n(Restrictions/Detail)','Days':'TR','Time':'09:35 am-10:50 am','Cap':'31','Act':'10','Rem':'21','Instructor':'Theodora Chaspari(P)','Date':'08/28-12/13','Location':'ETB 3002','Attribute':' '},
        {'Select':text,'CRN':'33086','Subj':'CSCE','Crse':'233','Sec':'400','Cmp':'CS','Cred':'3','Title':'MACHINE LEARNING\n\n\n(Restrictions/Detail)','Days':'TR','Time':'09:35 am-10:50 am','Cap':'31','Act':'10','Rem':'21','Instructor':'Theodora Chaspari(P)','Date':'08/28-12/13','Location':'ETB 3002','Attribute':' '},
        {'Select':text,'CRN':'33086','Subj':'CSCE','Crse':'233','Sec':'600','Cmp':'CS','Cred':'3','Title':'MACHINE LEARNING\n\n\n(Restrictions/Detail)','Days':'TR','Time':'09:35 am-10:50 am','Cap':'31','Act':'0','Rem':'21','Instructor':'Theodora Chaspari(P)','Date':'08/28-12/13','Location':'ETB 3002','Attribute':' '},


    ]
});