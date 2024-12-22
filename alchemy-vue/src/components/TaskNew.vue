<template>
    <div class="new-task">
        <h3>Nueva tarea</h3>
        <div>
          <input type="text" v-model="taskTitle" placeholder="título" />
        </div>
        <div>
          <textarea v-model="taskDescription" placeholder="descripción"></textarea>
        </div>
        <div class="button-container">
          <button @click="addTask" class="btn-addTask">Nueva tarea</button>
          <button @click="delAllTasks" class="btn-delAllTask">Eliminar todas</button>
        </div>
    </div>
</template>

<script>



export default {
  name: 'TaskNew',
  data() {
    const taskTitle = ''
    const taskDescription = ''
    return {taskTitle, taskDescription}
  },
  methods: {
    addTask() {
      this.$.emit('newTask', this.taskTitle, this.taskDescription)
      if (!this.taskTitle.length)
        return
      
      this.taskTitle = ''
      this.taskDescription = ''
    },
    delAllTasks() {
      this.$.emit('delAllTasks')
    }
  },
  props: {
  },
  emits: ['newTask', 'delAllTasks'],
}
</script>

<style lang="sass" scoped>
.new-task
  border: 1px solid #dce794
  border-radiuis: 100px
  margin-bottom: 20px
  padding: 10px
  display: inline-block
  width: 400px
  h3
    font-size: 20px
    font-weight: bold
    text-align: left
    padding-bottom: 8px
  input, textarea
    width: 100%
    border: 1px solid #ccc
    padding: 2px 6px
  input
    margin-bottom: 10px
  textarea
    resize: none
    height: 100px
  .button-container
    text-align: left
    display: flex
    justify-content: space-between 
    .btn-addTask
      background-color: #118311
      color: #fff
      padding: 2px 6px
      &:hover
        background-color: #1aa41a
    .btn-delAllTask
        background-color: #fc8686
        color: #fff
        padding: 2px 6px
        &:hover
          background-color: #ff0000

</style>