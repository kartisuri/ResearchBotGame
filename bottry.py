from subprocess import Popen, PIPE

def bot(request):
    process = Popen(["node", r"C:\Users\Karthik\Desktop\Research\bottry.js", request], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    return str(output).strip()
	
if __name__ == '__main__':
    a = bot('What is your name')
    print(a)