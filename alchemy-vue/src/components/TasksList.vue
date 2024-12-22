<template>
    <WaitProcess :waitShow="waitProcess"></WaitProcess>
    <div class="new-task-container">
      <TaskNew @newTask="newTask" @delAllTasks="delAllTasks"></TaskNew>
    </div>
    <div class="tasklist">
      <TaskSingle v-for="(task, idx) in tasks" :key="idx" :taskIndex="idx" :taskId="task.id" :taskTitle="task.title" :taskDescription="task.description"
        @updateTask="updateTask" @delTask="delTask"></TaskSingle>
    </div>
</template>

<script>
import TaskSingle from '@/components/TaskSingle.vue'
import TaskNew from './TaskNew.vue';
import PythonAlchemyTasks from '@/services/pythonAlchemyTasks.js';
import { useToast } from "vue-toastification"
import Swal from 'sweetalert2'
import WaitProcess from '@/components/ui/WaitProcess.vue'
import { toastSettings, sweetalerSettings } from '@/settings/ui.js'


const toast = useToast();

export default {
  name: 'TasksList',
  components: {
    TaskSingle,
    TaskNew,
    WaitProcess,
  },
  data() {
    const paTasks = new PythonAlchemyTasks()
    const tasks = [],
    waitProcess = false
    return {paTasks, tasks, waitProcess}
  },
  methods: {
    async newTask(title, description) {
      if (!title.length) {
        toast.error(`La tarea debe terner un título.`, toastSettings)
        return
      }
      if (!description.length)
        toast.warning(`La tarea está vacía.`, toastSettings)
      
      try {
        this.waitProcess = true
        const newTask = await this.paTasks.newTask(title, description)
        this.tasks.push(newTask)
        toast.success(`Tarea ${newTask.id} creada.`, toastSettings);
      }
      catch {
        toast.error(`Error al crear la nueva tarea.`, toastSettings)
      }
      finally {
        this.waitProcess = false
      }
    },
    async getTasks() {
      try {
        this.waitProcess = true
        this.tasks = await this.paTasks.getTasks()
      }
      catch {
        toast.error(`Error al listar las tareas.`, toastSettings)
      }
      finally {
        this.waitProcess = false
      }
    },
    async updateTask(index, id, title, description) {
      try {
        this.waitProcess = true
        const task = this.tasks[index]
        task.title = title
        task.description = description
        await this.paTasks.updateTask(id, title, description)
        toast.success(`Tarea ${id} modificada.`, toastSettings);
      }
      catch {
        toast.error(`Error al guardar la tarea ${id}`, toastSettings)
      }
      finally {
        this.waitProcess = false
      }
    },
    async delTask(index, id) {
      console.log(index, id)
      try {
        this.waitProcess = true
        await this.paTasks.deleteTask(id)
        this.tasks.splice(index, 1)
        toast.success(`Tarea ${id} eliminada.`, toastSettings);
      }
      catch {
        toast.error(`Error al eliminar la tarea ${id}`, toastSettings)
      }
      finally {
        this.waitProcess = false
      }
    },
    delAllTasks() {
      if (!this.tasks.length) {
        toast.warning('No existen tareas.', toastSettings);
        return
      }

      Swal.fire({...sweetalerSettings, text:'¿Desea eliminar todas las tareas?'})
        .then((result) => {
          if (result.isConfirmed) {
            this.waitProcess = true
            this.paTasks.deletaAllTasks()
            .then(() => {
              toast.success(`Eliminadas ${this.tasks.length} (todas).`, toastSettings);
              this.tasks = []
            })
            .catch(() => {
              toast.error('Error al eliminar todas las taresas.', toastSettings)
            })
            .finally(() => this.waitProcess = false)
          }
        })
    }
  },
  mounted() { 
    this.getTasks()
  },
}
</script>

<style lang="sass" scoped>
.new-task-container
  width: 800px
  text-align: center
.tasklist
  display: flex
  gap: 20px
  flex-wrap: wrap

</style>