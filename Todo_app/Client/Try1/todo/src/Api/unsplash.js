import axios from 'axios';

export default axios.create({
    baseURL: 'https://api.unsplash.com',
    headers: {
        Authorization:'Client-ID jgXEopIcHGu7pLjVQkE5F6KSGNzYr0spV7dk0uFpgHk'
    }
});