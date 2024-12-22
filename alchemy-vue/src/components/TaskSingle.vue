<template>
  <div class="task" :task-id="taskId" :task-index="taskIndex">
    <input type="text" :value="taskTitle" @change="changeTaskTitle" />
    <textarea :value="taskDescription" @change="changeTaskDescription"></textarea>
    <div class="taskdel"><button @click="$emit('delTask', taskIndex, taskId)">Eliminar</button></div>
  </div>
</template>

<script>
export default {
  name: 'TaskSingle',
  data() {
    return {}
  },
  methods: {
    changeTaskTitle(evt) {
      this.$emit('updateTask', this.taskIndex, this.taskId, evt.target.value, this.taskDescription)
    },
    changeTaskDescription(evt) {
      this.$emit('updateTask', this.taskIndex, this.taskId, this.taskTitle, evt.target.value)
    },
    /*
    // Definido directamente en el template
    delTask() {
      this.$emit('delTask', this.taskIndex, this.taskId)
    }
    */
  },
  props: {
    taskIndex: {
      type: Number
    },
    taskId: {
      type: Number
    },
    taskTitle: {
      type: String
    },
    taskDescription: {
      type: String
    }
  },
  computed: {

  },
  emits: ['updateTask', 'delTask', 'delTask'],
}
</script>

<style lang="sass" scoped>
.task
  background-color: #f7fdd2
  border: 1px solid #dce794
  display: flex
  flex-direction: column
  width: 250px
  border-radius: 5px
  input, textarea
    background-color: #f7fdd2
    padding: 4px 8px
    &:focus
      background-color: #fdf4c4
  input
    border: 0 solid #fff
    font-weight: bold
    border-top-left-radius: 5px
    border-top-right-radius: 5px
  textarea
    border: 0 solid #fff
    resize: none
    height: 100px
    border-bottom-left-radius: 5px
    border-bottom-right-radius: 5px
  .taskdel
    text-align: right
    button
      background-color: #fc8686
      color: #fff
      padding: 0px 8px
      border-radius: 5px
      &:hover
        background-color: #ff0000
    
</style>