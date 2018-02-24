pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        sh 'python -m unittest discover . "*test_solution.py"'
      }
    }
    stage('echo') {
      steps {
        input(message: 'Enter your name', id: 'name', ok: 'Good')
        echo 'Hello $name'
      }
    }
  }
}