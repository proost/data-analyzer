class Loader {
    constructor(outputStandard) {
        this.router = new Router();
        this.outputStandard = outputStandard;
    }

    getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    getFile(fileName) {
        let self = this;
        let excelName = outputStandardMap.get(self.outputStandard);
        self.router.getFile(fileName)
            .then(response => response.blob())
            .then(response => {
                let url = window.URL.createObjectURL(response);
                let a = document.createElement('a');
                a.href = url;
                a.download = excelName + '.xlsx';
                document.body.appendChild(a);
                a.click();
                a.remove();
            });
    }
}