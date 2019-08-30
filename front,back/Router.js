const BASEURL = '';

class Router {

    getFile(fileName) {
        let directoryUrl = BASEURL + 'url';
        let url = new URL(directoryUrl);
        url.search = new URLSearchParams(fileName);
        return fetch(url)
                .then(response => { 
                    if (response.ok) {
                        return response
                    } else {
                        console.log('Network response was not ok.');
                    }
                })
                .catch((error) => {
                    console.log('There has been a problem with fetch operation: ' + error.message);
                });
    }
}
