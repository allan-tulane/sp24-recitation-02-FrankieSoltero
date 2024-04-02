
from main import *

def test_simple_work():
    """ done. """
    assert simple_work_calc(10, 2, 2) == 36
    assert simple_work_calc(20, 3, 2) == 230
    assert simple_work_calc(30, 4, 2) == 650
    assert simple_work_calc(40, 5, 2) == 5390
    assert simple_work_calc(50, 6, 2) == 13592
    assert simple_work_calc(60, 7, 2) == 27416
    
def test_work():
    assert work_calc(10, 2, 2,lambda n: 1) == 15
    assert work_calc(20, 1, 2, lambda n: n*n) == 530
    assert work_calc(30, 3, 2, lambda n: n) == 300
    assert work_calc(50, 2, 2, lambda n: 2*n) == 520
    assert work_calc(40, 1, 2, lambda n: n * n) == 2130
    assert work_calc(60, 3, 2, lambda n: n) == 960

def test_compare_work():
  def cur_work(a,b,f):
     return lambda n: work_calc(n,a,b,f)
  
  res = compare_work(cur_work(2,2,lambda n: 1), cur_work(2,2,lambda n: n))
  print_Work_results(res)
  res = compare_work(cur_work(2,2,lambda n: n), cur_work(2,2,lambda n: n*n))
  print_Work_results(res)
  
      
    # curry work_calc to create multiple work
    # functions that can be passed to compare_work
    
    # create work_fn1
    # create work_fn2

    
def test_compare_span():
    def cur_span(a,b,f):
      return lambda n: span_calc(n,a,b,f)
    res = compare_span(cur_span(2,2,lambda n: 1), cur_span(2,2,lambda n: n))
    print_Span_results(res)
    res = compare_span(cur_span(2,2,lambda n: n), cur_span(2,2,lambda n: n*n))
    print_Span_results(res)
                       

  
	# TODO
