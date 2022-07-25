function nameGrab(list){
    let stufflist = "";
    for(activity in list){
            stufflist += activity.name + " "
        }
    return stufflist
}






function nameGrab(list){
    let stufflist = "";
    for( i = 0; i <list.length; i++){
        stufflist += list[i].name + ", "
    }
    return stufflist
}
