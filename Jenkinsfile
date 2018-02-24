pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        sh 'python -m unittest discover . "*test_solution.py"'
      }
    }
  }
}