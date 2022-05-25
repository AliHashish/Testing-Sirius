import http from 'k6/http';
import { sleep } from 'k6'

export let options = {
    insecureSkipTLSVerify: true,
    noConnectionReuse: false,
    thresholds: {
        http_req_duration: ['p(95)<1050'] // el 1050 dyh milli seconds
                                         // checks if the fastest 95% have finished their requests in less than 1050 ms
    },
    stages: [
        // Below average load
        { duration: '2s', target: 50 },  // raises users from 0 to 50 in 2 minutes
        { duration: '2s', target: 50 },  // keeps users at that number for 5 minutes

        // Average load        
        { duration: '2s', target: 150 },  // raises users from 50 to 150 in 2 minutes
        { duration: '2s', target: 150 },  // keeps users at that number for 5 minutes

        // Above average load (server about to shut down)
        { duration: '2s', target: 250 },  // raises users from 150 to 250 in 2 minutes
        { duration: '2s', target: 250 },  // keeps users at that number for 5 minutes

        // This is even going further beyond
        { duration: '2s', target: 280 },  // raises users from 150 to 250 in 2 minutes
        { duration: '2s', target: 280 },  // keeps users at that number for 5 minutes

        // Recovery stage
        { duration: '2s', target: 0 },  // returns to 0 users.

        // ebtada yedrab 3nd 250
    ],
};

const API_BASE_URL = 'http://mysirius.me:3000/';
const requestHeaders = {
        //'Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyNjQ5NzZiYjIwYzdhMjMzNDFhNGUxYiIsImlhdCI6MTY1MDkyNDg3NywiZXhwIjoxNjU5NTY0ODc3fQ.S1ZBOjDv6TcU48AEmn-8nHkgGiasZfj6Id2kk9ocYS4', // dh el token bta3 boody
        'Authorization': 'Bearer ' +'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyNjg4ZWM5OWEzNjc3NWIzNDZlNmEyZCIsImlhdCI6MTY1MTAyMDMwNSwiZXhwIjoxNjU5NjYwMzA1fQ.nQusm1ETvwgOFceFbqu_BAG8F_uorveWD2LCGprh8pc', // dh el token bta3 user 0
};


export default () => {

    
    // dh el hy-get exectued by el virtual users
    // http.batch([
    // //     ['GET', `${API_BASE_URL}/home`],
    // //     ['GET', `${API_BASE_URL}/:username`],
    // //     ['GET', `${API_BASE_URL}/:username/notifications`],

    // //     ['GET', `${API_BASE_URL}/:username/messages`],
    // //     ['GET', `${API_BASE_URL}/:username`],
    //     ['GET', `${API_BASE_URL}/home/:tweetId/likeTweet`, params],

    //     // ['GET', `${API_BASE_URL}/:username`],
    //     // ['GET', `${API_BASE_URL}/home/:tweetId/getRetweets`],
    //     // ['GET', `${API_BASE_URL}/home/:tweetId/getLikers`],

    //     // ['GET', `${API_BASE_URL}/home/:tweetId/getTaggedUsers`],
    //     // ['GET', `${API_BASE_URL}/home/:tweetId/getReplies`],
    //     // ['GET', `${API_BASE_URL}/settings/profile`],

    //     // ['GET', `${API_BASE_URL}/Boody`],
    //     // ['GET', `${API_BASE_URL}/boody`],
    // ]);
    
    
    
    // http.get(`${API_BASE_URL}/Boody`,params);
    // const res = http.get('http://34.236.108.123:3000/Boody', params);
    const res = http.batch([
        { method: 'GET', url: API_BASE_URL+'/user0', params: { headers: requestHeaders } },
        { method: 'GET', url: API_BASE_URL+'/settings/profile', params: { headers: requestHeaders } },
        { method: 'GET', url: API_BASE_URL+'/user1', params: { headers: requestHeaders } },
        { method: 'GET', url: API_BASE_URL+'/home/:tweetId/likeTweet', params: { headers: requestHeaders } },
      ]);

    sleep(1)
};