import setuptools

version = '1.1.2'
setuptools.setup(
  name = 'kidbit_assistant',
  version = version,
  license='MIT',
  description = 'Design your Own Assistant',
  author = 'KidBit',
  author_email = 'kidbitacademy@gmail.com',   
  url = 'https://github.com/KidBit-Academy/kidbit_assistant',
  download_url = 'https://github.com/KidBit-Academy/kidbit_assistant/archive/refs/tags/v' + version + '.tar.gz',
  keywords = ['ALEXA', 'BOT', 'CODING', 'KIDS', 'KIDBIT', 'ASSISTANT'],  
  install_requires=[        
          'SpeechRecognition==3.8.1',
          'pywhatkit==5.3',
          'wikipedia==1.4.0',
          'pyjokes==0.6.0',
          'gnewsclient==1.12',
          'PyAudio==0.2.11'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
  packages=["kidbit_assistant"],
  python_requires=">=3.6",
)