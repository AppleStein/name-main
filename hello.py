def func():
    print('     This is func() in hello.py')
    print('     __name__ is', __name__)


#他からインポートされた場合は実行されない
if __name__ == '__main__': #コマンドから実行→mainが入る
    print("Start if __name__ == '__main__'")
    print('call func()')
    func()