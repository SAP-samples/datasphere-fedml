METRIC_FILE_NAME = 'eval_metrics.pkl'
MODEL_FILE_NAME = 'model.pkl'

BASE_QUERY = '''
    SELECT
      *
    FROM
      `{table}`
  '''