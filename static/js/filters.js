/**
 * Created by tao on 8/15/17.
 */
function availableCourse(obj){
    var tmp =[];
    var len = obj.length;
    for(var i=0;i<len;++i){
        if(obj[i]['Rem']===''||obj[i]['Rem']===' '||parseInt(obj[i]['Rem'])<=0){
            continue;
        }
        tmp.push(obj[i]);
    }
    return tmp;
}


function masterCourses(obj) {
    var tmp =[];
    var len = obj.length;
    for(var i =0;i<len;++i){
        if(obj[i]['Crse']===''||obj[i]['Crse']===' '||parseInt(obj[i]['Crse'])<600){
            continue;
        }
        tmp.push(obj[i]);
    }
    return tmp;
}

function dealwith(confirmed,masterConfirm,backup,classes){
    classes=angular.copy(backup);
    if(confirmed||masterConfirm){
        if(confirmed){
            classes=availableCourse(classes);
        }
        if(masterConfirm){
            classes=masterCourses(classes);
        }
    }
    return classes;
}