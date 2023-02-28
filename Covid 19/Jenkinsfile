pipeline{
    agent any

    stages{
        stage("Checkout"){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Vamsi-Cloudangles/Dimond_new.git']]])
            }
        }
        stage("build"){
            steps{
                git branch: 'main', url: 'https://github.com/Vamsi-Cloudangles/Dimond_new.git'
            }
        }
        stage("load data"){
            steps{
                sh 'python3 load_data.py'
            }
        }
        stage("data analysis"){
            steps{
                sh 'python3 data_analysis.py'
            }
        }
        stage("data cleaning"){
            steps{
                sh 'python3 data_cleaning.py'
            }
        }
        stage("data visualization"){
            steps{
                sh 'python3 data_visualization.py'
            }
        }
        stage("feature engineering"){
            steps{
                sh 'python3 feature_engineering.py'
            }
        }
        stage("feature selection"){
            steps{
                sh 'python3 feature_selection.py'
            }
        }
        stage("data preprocessing"){
            steps{
                sh 'python3 data_preprocessing.py'
            }
        }
        stage("model selection"){
            steps{
                sh 'pyhton3 model_selection.py'
            }
        }
        
    }
    post{
        always{
            emailext body:"summery", subject: "Pipeline Status", to: 'vamsi.muramreddy@cloudangles.com'
        }
    }
}
