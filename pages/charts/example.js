example();

function example() {

/*
var tasks = [
{"startDate":new Date("Sun Dec 09 01:36:45 EST 2012"),"endDate":new Date("Sun Dec 09 02:36:45 EST 2012"),"taskName":"Invest in infra to pump RW","status":"RUNNING"},
{"startDate":new Date("Sun Dec 09 04:56:32 EST 2012"),"endDate":new Date("Sun Dec 09 06:35:47 EST 2012"),"taskName":"Invest in infra to pump RW","status":"RUNNING"},
{"startDate":new Date("Sun Dec 09 06:29:53 EST 2012"),"endDate":new Date("Sun Dec 09 06:34:04 EST 2012"),"taskName":"Invest in infra to pump RW","status":"RUNNING"},
{"startDate":new Date("Sun Dec 09 05:35:21 EST 2012"),"endDate":new Date("Sun Dec 09 06:21:22 EST 2012"),"taskName":"P Job","status":"RUNNING"},
{"startDate":new Date("Sun Dec 09 05:00:06 EST 2012"),"endDate":new Date("Sun Dec 09 05:05:07 EST 2012"),"taskName":"D Job","status":"RUNNING"},
{"startDate":new Date("Sun Dec 09 03:46:59 EST 2012"),"endDate":new Date("Sun Dec 09 04:54:19 EST 2012"),"taskName":"P Job","status":"RUNNING"},
{"startDate":new Date("Sun Dec 09 04:02:45 EST 2012"),"endDate":new Date("Sun Dec 09 04:48:56 EST 2012"),"taskName":"N Job","status":"RUNNING"},
{"startDate":new Date("Sun Dec 09 03:27:35 EST 2012"),"endDate":new Date("Sun Dec 09 03:58:43 EST 2012"),"taskName":"E Job","status":"SUCCEEDED"},
{"startDate":new Date("Sun Dec 09 01:40:11 EST 2012"),"endDate":new Date("Sun Dec 09 03:26:35 EST 2012"),"taskName":"A Job","status":"SUCCEEDED"},
{"startDate":new Date("Sun Dec 09 03:00:03 EST 2012"),"endDate":new Date("Sun Dec 09 03:09:51 EST 2012"),"taskName":"D Job","status":"SUCCEEDED"},
{"startDate":new Date("Sun Dec 09 01:21:00 EST 2012"),"endDate":new Date("Sun Dec 09 02:51:42 EST 2012"),"taskName":"P Job","status":"SUCCEEDED"},
{"startDate":new Date("Sun Dec 09 01:08:42 EST 2012"),"endDate":new Date("Sun Dec 09 01:33:42 EST 2012"),"taskName":"N Job","status":"FAILED"},
{"startDate":new Date("Sun Dec 09 00:27:15 EST 2012"),"endDate":new Date("Sun Dec 09 00:54:56 EST 2012"),"taskName":"E Job","status":"SUCCEEDED"},
{"startDate":new Date("Sun Dec 09 00:29:48 EST 2012"),"endDate":new Date("Sun Dec 09 00:44:50 EST 2012"),"taskName":"D Job","status":"SUCCEEDED"},
{"startDate":new Date("Sun Dec 09 07:39:21 EST 2012"),"endDate":new Date("Sun Dec 09 07:43:22 EST 2012"),"taskName":"P Job","status":"RUNNING"},
{"startDate":new Date("Sun Dec 09 07:00:06 EST 2012"),"endDate":new Date("Sun Dec 09 07:05:07 EST 2012"),"taskName":"D Job","status":"RUNNING"},
{"startDate":new Date("Sun Dec 09 08:46:59 EST 2012"),"endDate":new Date("Sun Dec 09 09:54:19 EST 2012"),"taskName":"P Job","status":"RUNNING"},
{"startDate":new Date("Sun Dec 09 09:02:45 EST 2012"),"endDate":new Date("Sun Dec 09 09:48:56 EST 2012"),"taskName":"N Job","status":"RUNNING"},
{"startDate":new Date("Sun Dec 09 08:27:35 EST 2012"),"endDate":new Date("Sun Dec 09 08:58:43 EST 2012"),"taskName":"E Job","status":"SUCCEEDED"},
{"startDate":new Date("Sun Dec 09 08:40:11 EST 2012"),"endDate":new Date("Sun Dec 09 08:46:35 EST 2012"),"taskName":"A Job","status":"SUCCEEDED"},
{"startDate":new Date("Sun Dec 09 08:00:03 EST 2012"),"endDate":new Date("Sun Dec 09 08:09:51 EST 2012"),"taskName":"D Job","status":"SUCCEEDED"},
{"startDate":new Date("Sun Dec 09 10:21:00 EST 2012"),"endDate":new Date("Sun Dec 09 10:51:42 EST 2012"),"taskName":"P Job","status":"SUCCEEDED"},
{"startDate":new Date("Sun Dec 09 11:08:42 EST 2012"),"endDate":new Date("Sun Dec 09 11:33:42 EST 2012"),"taskName":"N Job","status":"FAILED"},
{"startDate":new Date("Sun Dec 09 12:27:15 EST 2012"),"endDate":new Date("Sun Dec 09 12:54:56 EST 2012"),"taskName":"E Job","status":"SUCCEEDED"},
{"startDate":new Date("Sat Dec 08 23:12:24 EST 2012"),"endDate":new Date("Sun Dec 09 00:26:13 EST 2012"),"taskName":"A Job","status":"KILLED"}];
*/



    var tasks = [
        {"startDate":"2000","endDate":"2001","taskName":"Business as usual","status":"RUNNING"},
        {"startDate":"2001","endDate":"2002","taskName":"Business as usual","status":"RUNNING"},
        {"startDate":"2002","endDate":"2003","taskName":"Increase surface storage","status":"RUNNING"},
        {"startDate":"2003","endDate":"2004","taskName":"Increase amount of SW","status":"RUNNING"},
        {"startDate":"2004","endDate":"2005","taskName":"Increase amount of SW","status":"RUNNING"},
        {"startDate":"2005","endDate":"2006","taskName":"Increase amount of SW","status":"RUNNING"},
        {"startDate":"2006","endDate":"2007","taskName":"Increase surface storage","status":"RUNNING"},
        {"startDate":"2007","endDate":"2008","taskName":"Increase amount of SW","status":"RUNNING"},
        {"startDate":"2008","endDate":"2009","taskName":"Increase amount of SW","status":"RUNNING"},
        {"startDate":"2009","endDate":"2010","taskName":"Increase amount of SW","status":"RUNNING"},
        {"startDate":"2010","endDate":"2011","taskName":"Increase amount of GW","status":"RUNNING"},
        {"startDate":"2010","endDate":"2011","taskName":"Increase surface storage","status":"RUNNING"},
        {"startDate":"2011","endDate":"2012","taskName":"Increase amount of SW","status":"RUNNING"},
        {"startDate":"2012","endDate":"2013","taskName":"Increase amount of SW","status":"RUNNING"},
       ];


    var tasks0 = [
        {"startDate":"2000","endDate":"2001","taskName":"Increase amount of SW","status":"FAILED"},
        {"startDate":"2001","endDate":"2002","taskName":"Increase amount of SW","status":"FAILED"},
        {"startDate":"2002","endDate":"2003","taskName":"Increase amount of SW","status":"FAILED"},
        {"startDate":"2003","endDate":"2004","taskName":"Increase amount of SW","status":"FAILED"},
        {"startDate":"2004","endDate":"2005","taskName":"Increase amount of SW","status":"FAILED"},
        {"startDate":"2005","endDate":"2006","taskName":"Increase amount of RW","status":"FAILED"},
        {"startDate":"2006","endDate":"2007","taskName":"Increase amount of RW","status":"FAILED"},
        {"startDate":"2007","endDate":"2008","taskName":"Increase amount of SW","status":"FAILED"},
        {"startDate":"2008","endDate":"2009","taskName":"Increase amount of RW","status":"FAILED"},
        {"startDate":"2009","endDate":"2010","taskName":"Increase amount of RW","status":"FAILED"},
        {"startDate":"2010","endDate":"2011","taskName":"Increase amount of RW","status":"FAILED"},
        {"startDate":"2011","endDate":"2012","taskName":"Increase amount of RW","status":"FAILED"},
        {"startDate":"2012","endDate":"2013","taskName":"Increase amount of RW","status":"FAILED"},
    ];


    var tasks1 = [
        {"startDate":"2000","endDate":"2001","taskName":"Business as usual","status":"SUCCEEDED"},
        {"startDate":"2001","endDate":"2002","taskName":"Business as usual","status":"SUCCEEDED"},
        {"startDate":"2002","endDate":"2003","taskName":"Increase amount of GW","status":"SUCCEEDED"},
        {"startDate":"2003","endDate":"2004","taskName":"Increase amount of GW","status":"SUCCEEDED"},
        {"startDate":"2004","endDate":"2005","taskName":"Increase amount of GW","status":"SUCCEEDED"},
        {"startDate":"2005","endDate":"2006","taskName":"Increase amount of GW","status":"SUCCEEDED"},
        {"startDate":"2006","endDate":"2007","taskName":"Increase surface storage","status":"SUCCEEDED"},
        {"startDate":"2007","endDate":"2008","taskName":"Increase amount of SW","status":"SUCCEEDED"},
        {"startDate":"2008","endDate":"2009","taskName":"Increase amount of SW","status":"SUCCEEDED"},
        {"startDate":"2009","endDate":"2010","taskName":"Increase amount of SW","status":"SUCCEEDED"},
        {"startDate":"2010","endDate":"2011","taskName":"Increase amount of SW","status":"SUCCEEDED"},
        {"startDate":"2010","endDate":"2011","taskName":"Increase surface storage","status":"SUCCEEDED"},
        {"startDate":"2011","endDate":"2012","taskName":"Increase amount of SW","status":"SUCCEEDED"},
        {"startDate":"2012","endDate":"2013","taskName":"Increase amount of SW","status":"SUCCEEDED"},
    ];


    var tasks2 = [
        {"startDate":"2000","endDate":"2001","taskName":"Business as usual","status":"SUCCEEDED"},
        {"startDate":"2001","endDate":"2002","taskName":"Business as usual","status":"SUCCEEDED"},
        {"startDate":"2002","endDate":"2003","taskName":"Business as usual","status":"SUCCEEDED"},
        {"startDate":"2003","endDate":"2004","taskName":"Business as usual","status":"SUCCEEDED"},
        {"startDate":"2004","endDate":"2005","taskName":"Decrease total capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2005","endDate":"2006","taskName":"Decrease total capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2006","endDate":"2007","taskName":"Decrease total capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2007","endDate":"2008","taskName":"Decrease total capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2008","endDate":"2009","taskName":"Decrease total capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2009","endDate":"2010","taskName":"Decrease total capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2010","endDate":"2011","taskName":"Decrease total capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2011","endDate":"2012","taskName":"Decrease total capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2012","endDate":"2013","taskName":"Decrease total capacity by 20%","status":"SUCCEEDED"},
    ];

    var tasks3 = [
        {"startDate":"2000","endDate":"2001","taskName":"Business as usual","status":"SUCCEEDED"},
        {"startDate":"2001","endDate":"2002","taskName":"Business as usual","status":"SUCCEEDED"},
        {"startDate":"2002","endDate":"2003","taskName":"Business as usual","status":"SUCCEEDED"},
        {"startDate":"2003","endDate":"2004","taskName":"Business as usual","status":"SUCCEEDED"},
        {"startDate":"2004","endDate":"2005","taskName":"Increase capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2005","endDate":"2006","taskName":"Increase capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2006","endDate":"2007","taskName":"Increase capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2007","endDate":"2008","taskName":"Increase capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2008","endDate":"2009","taskName":"Increase capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2009","endDate":"2010","taskName":"Increase capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2010","endDate":"2011","taskName":"Increase capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2011","endDate":"2012","taskName":"Increase capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2012","endDate":"2013","taskName":"Increase capacity by 20%","status":"SUCCEEDED"},
    ];



    var tasks4 = [
        {"startDate":"2000","endDate":"2001","taskName":"Business as usual","status":"SUCCEEDED"},
        {"startDate":"2001","endDate":"2002","taskName":"Business as usual","status":"SUCCEEDED"},
        {"startDate":"2002","endDate":"2003","taskName":"Business as usual","status":"SUCCEEDED"},
        {"startDate":"2003","endDate":"2004","taskName":"Business as usual","status":"SUCCEEDED"},
        {"startDate":"2004","endDate":"2005","taskName":"Increase capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2005","endDate":"2006","taskName":"Increase capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2006","endDate":"2007","taskName":"Increase capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2007","endDate":"2008","taskName":"Increase capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2008","endDate":"2009","taskName":"Increase capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2009","endDate":"2010","taskName":"Increase capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2010","endDate":"2011","taskName":"Increase capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2011","endDate":"2012","taskName":"Increase capacity by 20%","status":"SUCCEEDED"},
        {"startDate":"2012","endDate":"2013","taskName":"Increase capacity by 20%","status":"SUCCEEDED"},
    ];


    var tasks5 = [
        {"startDate":"2000","endDate":"2001","taskName":"Business as usual","status":"KILLED"},
        {"startDate":"2001","endDate":"2002","taskName":"Business as usual","status":"KILLED"},
        {"startDate":"2002","endDate":"2003","taskName":"Increase capacity by 20%","status":"KILLED"},
        {"startDate":"2003","endDate":"2004","taskName":"Increase capacity by 20%","status":"KILLED"},
        {"startDate":"2004","endDate":"2005","taskName":"Increase capacity by 20%%","status":"KILLED"},
        {"startDate":"2005","endDate":"2006","taskName":"Increase capacity by 20%","status":"KILLED"},
        {"startDate":"2005","endDate":"2006","taskName":"Invest in infra to pump RW","status":"KILLED"},
        {"startDate":"2006","endDate":"2007","taskName":"Increase capacity by 20%","status":"KILLED"},
        {"startDate":"2006","endDate":"2007","taskName":"Invest in infra to pump RW","status":"KILLED"},
        {"startDate":"2007","endDate":"2008","taskName":"Increase capacity by 20%","status":"KILLED"},
        {"startDate":"2007","endDate":"2008","taskName":"Invest in infra to pump RW","status":"KILLED"},
        {"startDate":"2008","endDate":"2009","taskName":"Pump RW to farmers/diaries","status":"KILLED"},
        {"startDate":"2009","endDate":"2010","taskName":"Pump RW to farmers/diaries","status":"KILLED"},
        {"startDate":"2010","endDate":"2011","taskName":"Pump RW to farmers/diaries","status":"KILLED"},
        {"startDate":"2011","endDate":"2012","taskName":"Pump RW to farmers/diaries","status":"KILLED"},
        {"startDate":"2012","endDate":"2013","taskName":"Pump RW to farmers/diaries","status":"KILLED"},
    ];



    var tasks6 = [
        {"startDate":"2000","endDate":"2001","taskName":"Business as usual","status":"RUNNING"},
        {"startDate":"2001","endDate":"2002","taskName":"Business as usual","status":"RUNNING"},
        {"startDate":"2002","endDate":"2003","taskName":"Increase surface storage","status":"RUNNING"},
        {"startDate":"2003","endDate":"2004","taskName":"Increase amount of SW","status":"RUNNING"},
        {"startDate":"2004","endDate":"2005","taskName":"Increase amount of SW","status":"RUNNING"},
        {"startDate":"2005","endDate":"2006","taskName":"Increase amount of SW","status":"RUNNING"},
        {"startDate":"2006","endDate":"2007","taskName":"Increase surface storage","status":"RUNNING"},
        {"startDate":"2007","endDate":"2008","taskName":"Increase amount of SW","status":"RUNNING"},
        {"startDate":"2008","endDate":"2009","taskName":"Increase amount of SW","status":"RUNNING"},
        {"startDate":"2009","endDate":"2010","taskName":"Increase amount of SW","status":"RUNNING"},
        {"startDate":"2010","endDate":"2011","taskName":"Increase amount of GW","status":"RUNNING"},
        {"startDate":"2010","endDate":"2011","taskName":"Increase surface storage","status":"RUNNING"},
        {"startDate":"2011","endDate":"2012","taskName":"Increase amount of SW","status":"RUNNING"},
        {"startDate":"2012","endDate":"2013","taskName":"Increase amount of SW","status":"RUNNING"},
        {"startDate":"2000","endDate":"2001","taskName":"Business as usual","status":"SUCCEEDED"},
        {"startDate":"2001","endDate":"2002","taskName":"Business as usual","status":"SUCCEEDED"},
        {"startDate":"2002","endDate":"2003","taskName":"Increase amount of GW","status":"SUCCEEDED"},
        {"startDate":"2003","endDate":"2004","taskName":"Increase amount of GW","status":"SUCCEEDED"},
        {"startDate":"2004","endDate":"2005","taskName":"Increase amount of GW","status":"SUCCEEDED"},
        {"startDate":"2005","endDate":"2006","taskName":"Increase amount of GW","status":"SUCCEEDED"},
        {"startDate":"2006","endDate":"2007","taskName":"Increase surface storage","status":"SUCCEEDED"},
        {"startDate":"2007","endDate":"2008","taskName":"Increase amount of SW","status":"SUCCEEDED"},
        {"startDate":"2008","endDate":"2009","taskName":"Increase amount of SW","status":"SUCCEEDED"},
        {"startDate":"2009","endDate":"2010","taskName":"Increase amount of SW","status":"SUCCEEDED"},
        {"startDate":"2010","endDate":"2011","taskName":"Increase amount of SW","status":"SUCCEEDED"},
        {"startDate":"2010","endDate":"2011","taskName":"Increase surface storage","status":"SUCCEEDED"},
        {"startDate":"2011","endDate":"2012","taskName":"Increase amount of SW","status":"SUCCEEDED"},
        {"startDate":"2012","endDate":"2013","taskName":"Increase amount of SW","status":"SUCCEEDED"},
        {"startDate":"2000","endDate":"2001","taskName":"Business as usual","status":"ACTOR1"},
        {"startDate":"2001","endDate":"2002","taskName":"Business as usual","status":"ACTOR1"},
        {"startDate":"2002","endDate":"2003","taskName":"Business as usual","status":"ACTOR1"},
        {"startDate":"2003","endDate":"2004","taskName":"Business as usual","status":"ACTOR1"},
        {"startDate":"2004","endDate":"2005","taskName":"Decrease total capacity by 20%","status":"ACTOR1"},
        {"startDate":"2005","endDate":"2006","taskName":"Decrease total capacity by 20%","status":"ACTOR1"},
        {"startDate":"2006","endDate":"2007","taskName":"Decrease total capacity by 20%","status":"ACTOR1"},
        {"startDate":"2007","endDate":"2008","taskName":"Decrease total capacity by 20%","status":"ACTOR1"},
        {"startDate":"2008","endDate":"2009","taskName":"Decrease total capacity by 20%","status":"ACTOR1"},
        {"startDate":"2009","endDate":"2010","taskName":"Decrease total capacity by 20%","status":"ACTOR1"},
        {"startDate":"2010","endDate":"2011","taskName":"Decrease total capacity by 20%","status":"ACTOR1"},
        {"startDate":"2011","endDate":"2012","taskName":"Decrease total capacity by 20%","status":"ACTOR1"},
        {"startDate":"2012","endDate":"2013","taskName":"Decrease total capacity by 20%","status":"ACTOR1"},
        {"startDate":"2000","endDate":"2001","taskName":"Business as usual","status":"ACTOR2"},
        {"startDate":"2001","endDate":"2002","taskName":"Business as usual","status":"ACTOR2"},
        {"startDate":"2002","endDate":"2003","taskName":"Business as usual","status":"ACTOR2"},
        {"startDate":"2003","endDate":"2004","taskName":"Business as usual","status":"ACTOR2"},
        {"startDate":"2004","endDate":"2005","taskName":"Increase capacity by 20%","status":"ACTOR2"},
        {"startDate":"2005","endDate":"2006","taskName":"Increase capacity by 20%","status":"ACTOR2"},
        {"startDate":"2006","endDate":"2007","taskName":"Increase capacity by 20%","status":"ACTOR2"},
        {"startDate":"2007","endDate":"2008","taskName":"Increase capacity by 20%","status":"ACTOR2"},
        {"startDate":"2008","endDate":"2009","taskName":"Increase capacity by 20%","status":"ACTOR2"},
        {"startDate":"2009","endDate":"2010","taskName":"Increase capacity by 20%","status":"ACTOR2"},
        {"startDate":"2010","endDate":"2011","taskName":"Increase capacity by 20%","status":"ACTOR2"},
        {"startDate":"2011","endDate":"2012","taskName":"Increase capacity by 20%","status":"ACTOR2"},
        {"startDate":"2012","endDate":"2013","taskName":"Increase capacity by 20%","status":"ACTOR2"},
        {"startDate":"2000","endDate":"2001","taskName":"Business as usual","status":"ACTOR3"},
        {"startDate":"2001","endDate":"2002","taskName":"Business as usual","status":"ACTOR3"},
        {"startDate":"2002","endDate":"2003","taskName":"Business as usual","status":"ACTOR3"},
        {"startDate":"2003","endDate":"2004","taskName":"Business as usual","status":"ACTOR3"},
        {"startDate":"2004","endDate":"2005","taskName":"Increase capacity by 20%","status":"ACTOR3"},
        {"startDate":"2005","endDate":"2006","taskName":"Increase capacity by 20%","status":"ACTOR3"},
        {"startDate":"2006","endDate":"2007","taskName":"Increase capacity by 20%","status":"ACTOR3"},
        {"startDate":"2007","endDate":"2008","taskName":"Increase capacity by 20%","status":"ACTOR3"},
        {"startDate":"2008","endDate":"2009","taskName":"Increase capacity by 20%","status":"ACTOR3"},
        {"startDate":"2009","endDate":"2010","taskName":"Increase capacity by 20%","status":"ACTOR3"},
        {"startDate":"2010","endDate":"2011","taskName":"Increase capacity by 20%","status":"ACTOR3"},
        {"startDate":"2011","endDate":"2012","taskName":"Increase capacity by 20%","status":"ACTOR3"},
        {"startDate":"2012","endDate":"2013","taskName":"Increase capacity by 20%","status":"ACTOR3"},
        {"startDate":"2000","endDate":"2001","taskName":"Business as usual","status":"KILLED"},
        {"startDate":"2001","endDate":"2002","taskName":"Business as usual","status":"KILLED"},
        {"startDate":"2002","endDate":"2003","taskName":"Increase capacity by 20%","status":"KILLED"},
        {"startDate":"2003","endDate":"2004","taskName":"Increase capacity by 20%","status":"KILLED"},
        {"startDate":"2004","endDate":"2005","taskName":"Increase capacity by 20%%","status":"KILLED"},
        {"startDate":"2005","endDate":"2006","taskName":"Increase capacity by 20%","status":"KILLED"},
        {"startDate":"2005","endDate":"2006","taskName":"Invest in infra to pump RW","status":"KILLED"},
        {"startDate":"2006","endDate":"2007","taskName":"Increase capacity by 20%","status":"KILLED"},
        {"startDate":"2006","endDate":"2007","taskName":"Invest in infra to pump RW","status":"KILLED"},
        {"startDate":"2007","endDate":"2008","taskName":"Increase capacity by 20%","status":"KILLED"},
        {"startDate":"2007","endDate":"2008","taskName":"Invest in infra to pump RW","status":"KILLED"},
        {"startDate":"2008","endDate":"2009","taskName":"Pump RW to farmers/diaries","status":"KILLED"},
        {"startDate":"2009","endDate":"2010","taskName":"Pump RW to farmers/diaries","status":"KILLED"},
        {"startDate":"2010","endDate":"2011","taskName":"Pump RW to farmers/diaries","status":"KILLED"},
        {"startDate":"2011","endDate":"2012","taskName":"Pump RW to farmers/diaries","status":"KILLED"},
        {"startDate":"2012","endDate":"2013","taskName":"Pump RW to farmers/diaries","status":"KILLED"},
    ];




    var taskStatus = {
    "SUCCEEDED" : "bar",
    "FAILED" : "bar-failed",
    "RUNNING" : "bar-running",
    "KILLED" : "bar-killed",
        "ACTOR1": "actor-1",
        "ACTOR2": "actor-2",
        "ACTOR3": "actor-3"
};

var taskNames = [ "Business as usual", "Increase capacity by 20%", "Decrease total capacity by 20%", "Increase amount of SW", "Increase amount of GW", "Increase amount of RW", "Decrease amount of SW", "Decrease amount of GW", "Invest in renewable energy sources", "Pump RW to farmers/diaries", "Increase surface storage", "Invest in infra to pump RW" ];

tasks.sort(function(a, b) {
    return a.endDate - b.endDate;
});
var maxDate = tasks[tasks.length - 1].endDate;
tasks.sort(function(a, b) {
    return a.startDate - b.startDate;
});
var minDate = tasks[0].startDate;

var format = "%Y";

var gantt = d3.gantt().taskTypes(taskNames).taskStatus(taskStatus).tickFormat(format);
gantt(tasks);

    var gantt = d3.gantt().taskTypes(taskNames).taskStatus(taskStatus).tickFormat(format);
    gantt(tasks0);

    var gantt = d3.gantt().taskTypes(taskNames).taskStatus(taskStatus).tickFormat(format);
    gantt(tasks1);

    var gantt = d3.gantt().taskTypes(taskNames).taskStatus(taskStatus).tickFormat(format);
    gantt(tasks2);

    var gantt = d3.gantt().taskTypes(taskNames).taskStatus(taskStatus).tickFormat(format);
    gantt(tasks3);

    var gantt = d3.gantt().taskTypes(taskNames).taskStatus(taskStatus).tickFormat(format);
    gantt(tasks4);

    var gantt = d3.gantt().taskTypes(taskNames).taskStatus(taskStatus).tickFormat(format);
    gantt(tasks5);

    var gantt = d3.gantt().taskTypes(taskNames).taskStatus(taskStatus).tickFormat(format);
    gantt(tasks6);


};

