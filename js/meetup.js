"use strict";

class Meetup {
    constructor(organizer) {
        this.organizer = organizer;
    }
}

class TechMeet extends Meetup {
    constructor(organizer, techTopic) {
        super(organizer);
        this.techTopic = techTopic;
    }
}

const js = new TechMeet("JS Enterprise", "Microservices");
console.log(js.organizer, js.techTopic);
