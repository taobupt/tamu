'use strict';
var animateApp = angular.module('animateApp', ['ui.router', 'ngAnimate','ng-backstretch','ngMaterial','ngSanitize','ngProgress','ui.navbar','ngStorage']);
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
        .state('yourCourses',{
            url: '/yourCourses',
            templateUrl:'static/partials/yourCourses.html',
            controller:'yourCoursesController',
            resolve: {
               accessToken: ['$localStorage','$location','$mdDialog', function($localStorage,$location,$mdDialog){
                   if($localStorage.accessToken){
                        return $localStorage.accessToken;
                   }
                   else {
                        $location.path('/home');
                        return;
                   }
                }]
            }
        })
        .state('classes',{
            url: '/classes',
            templateUrl:'static/partials/classes.html',
            controller:'classesController',
            resolve: {
               accessToken: ['$localStorage','$location','$mdDialog', function($localStorage,$location,$mdDialog){
                   if($localStorage.accessToken){
                        return $localStorage.accessToken;
                   }
                   else {
                        $location.path('/home');
                        return;
                   }
                }]
            }
        })
});


// CONTROLLERS ============================================
// home page controller
animateApp.controller('mainController', function($rootScope,$scope,$http,$state,$mdDialog,ngProgressFactory,$localStorage) {
    $scope.images = [
    '/static/img/login/1.jpg',
    '/static/img/login/2.jpg'
  ];
    $rootScope.user={
        'NetID':'taobupt',
        'password':''
    };
    $scope.progressbar = ngProgressFactory.createInstance();
    $scope.progressbar.setColor("#0000ff");
    $scope.submitForm = function() {
        if ($scope.loginForm.$valid) {
            $scope.progressbar.start();
            $http({
                url:'http://127.0.0.1:5000/login',
                method:'post',
                params:{'NetID':$rootScope.user.NetID,'password':$rootScope.user.password}
            }).then(function (response) {
                $scope.progressbar.complete();
                var error = response.data;
                if (error===null){
                    $localStorage.accessToken = 'taobupt';
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
                $scope.progressbar.complete();
                window.alert(error);
            })
        }
    }
});

// about page controller
animateApp.controller('yourCoursesController', function($scope,$rootScope,$sce,$http,ngProgressFactory,$localStorage) {
    var text = "<input type='button' value='Drop' class='btn btn-warning btn-xs'>";
    text = $sce.trustAsHtml(text);
    if($localStorage.accessToken && ($rootScope.yourCourses===undefined||$rootScope.yourCourses.length==0)){
        $scope.progressbar = ngProgressFactory.createInstance();
        $scope.progressbar.setColor("brickred");
        $scope.progressbar.start();
        $http({
            url:"http://127.0.0.1:5000/getYourCourses",
            method:'GET'
        }).then(function (response) {
            $scope.progressbar.complete();
            $rootScope.yourCourses=[];
            var data = response.data;
            var d = {'Status':'**Web Registered** on Apr 07, 2017','Action':text,'CRN':'31266','Subj':'CSCE','Crse':'634','Sec':'600','Level':'Graduate','Cred':'3','Title':'INTELL USER INTERFACE'};
            var len = data.length;
            for(var i=0;i<len;++i){
                var ind =0;
                var tmp ={};
                for(var prop in d){
                    tmp[prop]=data[i][ind];
                    ind++;
                }
                tmp['Action']=text;
                $rootScope.yourCourses.push(tmp);
            }
        },function (error) {
            window.alert(error);
        })
    }
});

// contact page controller
animateApp.controller('contactController', function($scope) {
    $scope.pageClass = 'page-contact';
});

animateApp.controller('classesController', function($scope,$rootScope,$sce,$http,ngProgressFactory) {
    var text = "<input type='button' value='Select' class='btn btn-warning btn-xs'>";
    text = $sce.trustAsHtml(text);
    if($rootScope.availableCr===undefined){
        $scope.confirmed=false;
    }else{
        $scope.confirmed=$rootScope.availableCr;
    }
    if($rootScope.masterCr===undefined){
        $scope.masterConfirmed=false;
    }else{
        $scope.masterConfirmed=$rootScope.masterCr;
    }

    $scope.major="CSCE";

    $scope.change=function () {
        $rootScope.availableCr = $scope.confirmed;
        $rootScope.classes = angular.copy(dealwith($scope.confirmed,$scope.masterConfirmed,$rootScope.backup,$rootScope.classes));
    };

    $scope.masterFilter = function () {
        $rootScope.masterCr = $scope.masterConfirmed;
        $rootScope.classes = angular.copy(dealwith($scope.confirmed,$scope.masterConfirmed,$rootScope.backup,$rootScope.classes));
    };

    $scope.progressbar = ngProgressFactory.createInstance();
    $scope.progressbar.setColor("#ffff00");
    $scope.myFunc=function () {
        $scope.progressbar.start();
        $http({
            url:"http://127.0.0.1:5000/courses",
            method:'GET',
            params:{major:$scope.major}
        }).then(function (response) {
            $scope.progressbar.complete();
            var data = response.data;
            var d = {'Select':text,'CRN':'33086','Subj':'CSCE','Crse':'233','Sec':'600','Cmp':'CS','Cred':'3','Title':'MACHINE LEARNING\n\n\n(Restrictions/Detail)','Days':'TR','Time':'09:35 am-10:50 am','Cap':'31','Act':'10','Rem':'21','Instructor':'Theodora Chaspari(P)','Date':'08/28-12/13','Location':'ETB 3002','Attribute':' '}
            $rootScope.classes = [];
            var len = data.length;
            for(var i=0;i<len;++i){
                var ind =0;
                var tmp ={};
                for(var prop in d){
                    tmp[prop]=data[i][ind];
                    ind++;
                }
                if (tmp['Rem']!='' && tmp['Rem']!=' ' && parseInt(tmp['Rem'])>0){
                    tmp['Select']=text;
                }else{
                    tmp['Select']=' ';
                }
                $rootScope.classes.push(tmp);
            }
            $rootScope.backup=angular.copy($rootScope.classes);
            $rootScope.classes=angular.copy(dealwith($rootScope.availableCr,$rootScope.masterCr,$rootScope.backup,$rootScope.classes));
        },function (error) {
            $scope.progressbar.complete();
            window.alert(error);
        })
    }

});


//directives
animateApp.directive("removeMe", function($rootScope) {
      return {
            link:function(scope,element,attrs)
            {
                element.bind("click",function() {
                    element.remove();
                });
            }
      }
});