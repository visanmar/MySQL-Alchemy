export default class PythonAlchemyTasks {
    baseUrl = 'http://localhost:5000';

    async getTasks()  {
        const repsonse = await fetch(this.baseUrl + '/tasks', {method: 'GET'})
        const json = await repsonse.json()
        return json
    }
    
    async getTask(taskId) {
        const repsonse = await fetch(this.baseUrl + '/tasks/' + taskId, {method: 'GET'})
        const json = await repsonse.json()
        return json
    }

    async newTask(title, description) {
        const fetchOptions = {
            method: 'POST',
            headers: {
                //'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({"title":title, "description": description})
        }
        const repsonse = await fetch(this.baseUrl + '/tasks', fetchOptions)
        const json = await repsonse.json()
        return json  
    }
    async updateTask(taskId, title, description) {
        const fetchOptions = {
            method: 'PUT',
            headers: {
                //'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({"title":title, "description": description})
        }
        const repsonse = await fetch(this.baseUrl + '/tasks/' + taskId, fetchOptions)
        const json = await repsonse.json()
        return json
    }
    
    async deleteTask(taskId) {
        const repsonse = await fetch(this.baseUrl + '/tasks/' + taskId, {method: 'DELETE'})
        const json = await repsonse.json()
        return json
    }
    async deletaAllTasks() {
        try {
            const repsonse = await fetch(this.baseUrl + '/tasks/delete', {method: 'DELETE'})
            const json = await repsonse.json()
            return json
        }
        catch {
            throw new Error('Error al eliminar todas las taresas.')
        }
    }
}