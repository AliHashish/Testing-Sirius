import http from 'k6/http';
import { sleep } from 'k6'

export let options = {
    insecureSkipTLSVerify: true,
    noConnectionReuse: false,
    thresholds: {
        http_req_duration: ['p(95)<150'] // el 150 dyh milli seconds
                                         // checks if the fastest 95% have finished their requests in less than 150 ms
    },
    stages: [
        { duration: '45s', target: 5000},
        // { duration: '3s', target: 5},
        // { duration: '2s', target: 10},
        // { duration: '3s', target: 10},
        


        // { duration: '2m', target: 50 },  // raises users from 0 to 100 in 2 minutes
        // { duration: '5m', target: 50 },  // keeps users at that number for 5 minutes
        
        // { duration: '2m', target: 300 },  // raises users from 100 to 450 in 2 minutes
        // { duration: '5m', target: 300 },  // keeps users at that number for 5 minutes

        // { duration: '2m', target: 450 },  // raises users from 450 to 1000 in 2 minutes
        // { duration: '5m', target: 450 },  // keeps users at that number for 5 minutes
        
        // { duration: '10m', target: 0 },  // returns to 0 users. (Recovery stage)
    ],
};

const API_BASE_URL = 'http://34.236.108.123:3000';
const requestHeaders = {
        'Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyNjQ5NzZiYjIwYzdhMjMzNDFhNGUxYiIsImlhdCI6MTY1MDkyNDg3NywiZXhwIjoxNjU5NTY0ODc3fQ.S1ZBOjDv6TcU48AEmn-8nHkgGiasZfj6Id2kk9ocYS4',
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
        { method: 'GET', url: API_BASE_URL+'/boody', params: { headers: requestHeaders } },
        { method: 'GET', url: API_BASE_URL+'/settings/profile', params: { headers: requestHeaders } },
        { method: 'GET', url: API_BASE_URL+'/boody', params: { headers: requestHeaders } },
      ]);

    sleep(1)
};