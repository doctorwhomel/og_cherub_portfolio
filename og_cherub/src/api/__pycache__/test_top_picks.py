a
    Ҿ?b[  ?                   @   s?   d dl Zd dlm  mZ d dlmZmZm	Z	m
Z
 ddlmZmZmZmZ d dlZd dlmZ ededd?Zejd	d
gd?dd? ?ZdS )?    N)?	Blueprint?jsonify?abort?request?   )?User?Profile?Pick?db)?insert?	top_picksz
/top_picks)?
url_prefix? ?POST)?methodsc            
      C   sh  t jd } tj?? }tj?? }|D ]?}|j| kr"|}||k}|s?t?d|fd||f?dt	?
? v sjt?|?rtt?|?nddt	?
? v s?t?|?r?t?|?ndd? }dd|i }tt?|???d }q"|D ]}|j|jkr?tj?|? q?g }	|D ]j}|j|jkr?|j|jkr?|j|jkr?|j|jk?s*|jd	kr?t|j|jd
?}|	?|?? ? tj?|? q?tj??  t|	?S )N?id)?==)z%(py0)s == %(py2)s?user?p)Zpy0Zpy2zassert %(py4)sZpy4ZAll)Zpick_id?user_id)r   ?jsonr   ?query?allr	   r   ?
@pytest_ar?_call_reprcompare?@py_builtins?locals?_should_repr_global_name?	_saferepr?AssertionError?_format_explanationr   r
   ?session?deleteZuser_location?ageZmin_age?max_ageZgenderZseeking?append?	serialize?add?commitr   )
?activeZprofilesr   r   r   Z@py_assert1Z@py_format3Z@py_format5?pk?result? r,   ?wC:\Users\willi\Desktop\NucampFolder\Python\3-DevOps\week2\og_cherub_flask_portfolio\og_cherub\src\api\test_top_picks.py?populate_picks
   s,    



?$?
r.   )?builtinsr   ?_pytest.assertion.rewrite?	assertion?rewriter   ?flaskr   r   r   r   Zmodelsr   r   r	   r
   Z
sqlalchemyr   ?__name__?bp?router.   r,   r,   r,   r-   ?<module>   s   2